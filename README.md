# 🧠 Universal Research Assistant (RAG Engine)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Universal Research Assistant** is an intelligent, single-page web application that transforms static documents into an interactive knowledge base. Users can upload PDFs and web URLs to build a temporary, specialized RAG (Retrieval-Augmented Generation) pipeline on the fly.

Unlike generic chatbots, this tool grounds every answer in **your specific data**, providing accurate citations and eliminating hallucinations.

---

## 🚀 Key Features

### 🔍 Dynamic RAG Pipeline
* **Multi-Source Ingestion:** Upload multiple **PDFs** and **URLs** simultaneously to create a unified vector index.
* **Verifiable Answers:** Every AI response includes direct **citations** (source filenames or links), ensuring full transparency.

### 🤖 Gemini-Powered Analysis
* **Context-Aware QA:** Ask detailed questions and get answers based *only* on the provided context.
* **Smart Recommendations:** The engine analyzes your query and suggests **3 broader research topics** to help you explore the subject deeper.
* **Generative Tools:**
    * ✨ **Summarize:** Instantly generate high-level summaries of complex documents.
    * ✨ **Drafting Mode:** Expand AI answers into well-written paragraphs for reports or essays.

### 💻 Modern Interface
* **Split-View Dashboard:** A clean, responsive 2-column layout (built with **Tailwind CSS**) keeps your source list and chat interface visible at all times.

---

## 🛠️ Tech Stack

### Backend
* **Framework:** Flask (Python 3.9+)
* **LLM:** Google Gemini 1.5 Flash (via `langchain-google-genai`)
* **Orchestration:** LangChain (`RetrievalQA`, `PyPDFLoader`, `WebBaseLoader`)
* **Vector Store:** ChromaDB (In-memory similarity search)

### Frontend
* **Core:** Vanilla JavaScript (ES6+) for dynamic API interaction.
* **Styling:** Tailwind CSS for a modern, responsive design.

---

## ⚙️ How to Run Locally

You can run this entire application on your local machine in under 5 minutes.

### 1. Prerequisites
* Python 3.9+ installed on your system.
* A **Google Gemini API Key** (Get it from Google AI Studio).

### 2. Installation

Clone the repository and set up the environment:

```bash
# Clone the repo
git clone https://github.com/A-Kmr/universal-research-assistant.git
cd universal-research-assistant

# Create a virtual environment
python -m venv venv

# Activate venv (Windows)
.\venv\Scripts\activate

# Activate venv (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

### 3. Configuration
Create a .env file in the root directory and add your API key:

# Code snippet
GOOGLE_API_KEY="your_actual_api_key_goes_here"

### 4. Start the Application
Run the Flask server:

# Bash
python app.py
