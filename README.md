**Universal Research Assistant**

This project is an interactive, single-page web application that allows users to create a custom AI-powered research assistant. Users can upload their own PDF documents and provide website URLs to build a temporary, specialized knowledge base. They can then have a conversation with an AI (powered by Google's Gemini) that answers questions only based on the provided sources, ensuring all information is accurate, verifiable, and directly relevant to their research.

This tool moves beyond generic chatbots by creating a "RAG" (Retrieval-Augmented Generation) pipeline on the fly, complete with citations, conversational memory, and AI-powered writing tools.

**Key Features**

Dynamic Knowledge Base: Upload multiple PDFs and add multiple website URLs to create a custom knowledge base for any topic.

Conversational AI Chat: Engage in a natural, back-and-forth conversation with the AI. The assistant remembers previous questions and answers for contextual follow-ups.

Verifiable Answers: Every answer from the RAG pipeline is grounded in the provided sources. The UI displays which documents or links were used as sources for each response.

**Gemini-Powered Generative Tools**:

✨ Summarize All Sources: Instantly generate a high-level summary of all provided documents and websites.

✨ Extract Key Themes: Ask the AI to analyze the entire context and identify the main recurring themes and arguments.

✨ Draft a Paragraph: Expand any AI-generated answer into a well-written paragraph with a single click, bridging the gap from research to writing.

Modern Interface: A clean, responsive, two-column dashboard layout that keeps sources and the chat interface visible at all times.

**Tech Stack**

This application is built with a modern Python backend and a lightweight JavaScript frontend.

**Backend**:

Python 3.9+

Flask: To create the web server and API endpoints.

Google Gemini (via langchain-google-genai): The core large language model for generation and analysis.

LangChain: The primary framework for building the RAG pipeline.

ConversationalRetrievalChain: Manages the chat memory and retrieval.

PyPDFLoader & WebBaseLoader: To load and parse documents and websites.

Chroma: In-memory vector store for efficient similarity search.

**Frontend**:

HTML5

Tailwind CSS: For all styling and layout.

Vanilla JavaScript (ES6+): To handle all user interactions, API calls (fetch), and dynamic UI updates.

**How to Run This Project Locally**

You can run this entire application on your local machine.

**1. Prerequisites**

Python 3.9 or newer installed on your system.

A Google Gemini API Key.

**2. Setup**

Clone or download the repository:

git clone [https://github.com/your-username/universal-research-assistant.git](https://github.com/your-username/universal-research-assistant.git)
cd universal-research-assistant


**Create a virtual environment:**
This creates an isolated space for the project's libraries.

python -m venv venv


**Activate the virtual environment:**

On Windows (Command Prompt): .\venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

Install the required libraries:

pip install -r requirements.txt


**Create your environment file:**

Create a new file in the project folder named .env.

Open this file and add your API key like this:

GOOGLE_API_KEY="your_actual_api_key_goes_here"


**3. Run the Application**

Start the Flask server:
With your virtual environment still active, run:

python app.py
