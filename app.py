import os
import requests
import tempfile
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.chains import RetrievalQA

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# This will hold the RAG chain for a user's session.
# NOTE: This simple setup holds one chain in memory. For a multi-user production app,
# you would use a session-based approach to store chains for different users.
rag_chain = None

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process_sources():
    global rag_chain
    rag_chain = None # Reset the chain for each new build

    try:
        files = request.files.getlist('files')
        urls = request.form.getlist('urls')

        if not files and not urls:
            return jsonify({'error': 'No files or URLs provided.'}), 400

        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_docs = []
            for file in files:
                if file and file.filename.endswith('.pdf'):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(temp_dir, filename)
                    file.save(filepath)
                    loader = PyPDFLoader(filepath)
                    pdf_docs.extend(loader.load())
            
            def scrape_url(url):
                try:
                    response = requests.get(url, timeout=15)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.text, "html.parser")
                    return Document(page_content=soup.get_text(separator=" ", strip=True), metadata={"source": url})
                except requests.RequestException:
                    return None

            web_docs = [doc for doc in (scrape_url(url) for url in urls) if doc is not None]

            all_docs = pdf_docs + web_docs
            if not all_docs:
                return jsonify({'error': 'Could not process any of the provided sources.'}), 400

            splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
            chunks = splitter.split_documents(all_docs)

            embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
            vectorstore = Chroma.from_documents(chunks, embedding)
            
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)
            
            rag_chain = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vectorstore.as_retriever(),
                return_source_documents=True
            )

        return jsonify({'message': 'Knowledge base built successfully!'})

    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/query', methods=['POST'])
def handle_query():
    if not rag_chain:
        return jsonify({'error': 'Knowledge base not initialized. Please add sources first.'}), 400
    
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'No query provided.'}), 400

    try:
        # Get the direct answer and sources
        result = rag_chain.invoke(query)
        answer = result.get('result', 'No answer found.')
        sources = [doc.metadata.get('source', 'Unknown source') for doc in result.get('source_documents', [])]
        unique_sources = list(dict.fromkeys(sources))

        # Use the LLM to generate recommendations
        recommendation_prompt = f"Based on the following question: '{query}' and answer: '{answer}', suggest three related but broader topics for further research. Provide only the three topic names, separated by commas."
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.5)
        recommendations_str = llm.invoke(recommendation_prompt).content
        recommendations = [rec.strip() for rec in recommendations_str.split(',') if rec.strip()]

        return jsonify({
            'answer': answer,
            'sources': unique_sources,
            'recommendations': recommendations
        })

    except Exception as e:
        print(f"Error during query: {e}")
        return jsonify({'error': f'An error occurred while fetching the answer: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

