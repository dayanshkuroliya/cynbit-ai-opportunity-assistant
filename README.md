# Cynbit AI Opportunity Assistant

A RAG-based AI assistant designed for the Cynbit website to help visitors discover **Cynbit's services, products, technologies, projects, internships, and career opportunities** through natural-language conversations.

The assistant retrieves relevant information from a structured Cynbit knowledge base and uses a local language model to generate grounded responses.

---

## Project Overview

The **Cynbit AI Opportunity Assistant** is an AI-powered chatbot built as a website enhancement concept for Cynbit.

Instead of navigating through multiple pages to find information, visitors can simply ask questions such as:

> "What internships does Cynbit offer?"

> "What technologies does Cynbit use?"

> "What services does Cynbit provide?"

The system searches the available Cynbit knowledge base, retrieves the most relevant information, and generates a concise answer using an AI model.

---

## Problem Statement

Company websites contain a large amount of information about:

- Services
- Products
- Technologies
- Case studies
- Career opportunities
- Internships
- Job roles

Visitors may need to navigate through multiple pages to find the information they need.

The goal of this project is to provide a **single AI-powered interface** that makes this information easier and faster to discover.

---

##  Features

###  AI-Powered Chat

Users can ask questions using natural language instead of searching manually through website pages.

###  RAG-Based Information Retrieval

The assistant retrieves relevant information from the Cynbit knowledge base before generating an answer.

###  Source Visibility

The interface displays the knowledge files used to generate the response along with their relevance scores.

###  Local AI Model

The project currently uses a lightweight local language model, so an external paid LLM API is not required.

###  Business Information

Users can ask about:

- Cynbit services
- Products
- Technologies
- Case studies
- Development capabilities

###  Career Information

Users can ask about:

- Internships
- Job opportunities
- Required technologies
- Career-related information

###  Cynbit-Inspired UI

The frontend uses a clean interface inspired by Cynbit's visual identity, including:

- Teal color palette
- Pale blue background
- Peach accent
- Modern typography
- Responsive design

###  Responsive Interface

The application is designed to work on both desktop and mobile screens.

---

#  How It Works

The application follows a simple Retrieval-Augmented Generation pipeline:

```text
User Question
      │
      ▼
   React UI
      │
      ▼
   FastAPI
      │
      ▼
Question Embedding
      │
      ▼
Knowledge Retrieval
      │
      ▼
Relevant Cynbit Information
      │
      ▼
Local Language Model
      │
      ▼
Generated Answer
      │
      ▼
React Chat Interface
```

### RAG Pipeline

1. Cynbit information is stored in Markdown knowledge files.
2. The documents are divided into smaller chunks.
3. Each chunk is converted into an embedding using `all-MiniLM-L6-v2`.
4. When the user asks a question, the question is also converted into an embedding.
5. Cosine similarity is used to find relevant knowledge.
6. Keyword matching provides an additional retrieval signal.
7. The most relevant context is passed to the language model.
8. The language model generates a grounded response.
9. The frontend displays the answer and the retrieved sources.

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS
- Fetch API

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## AI / ML

- Hugging Face Transformers
- Sentence Transformers
- `all-MiniLM-L6-v2`
- `SmolLM2-360M-Instruct`
- NumPy
- Cosine Similarity

## Knowledge Base

- Markdown
- Structured Cynbit company information

## Development Tools

- Git
- GitHub
- VS Code

---

#  Project Structure

```text
cynbit-ai-opportunity-assistant/
│
├── backend/
│   │
│   ├── ai/
│   │   ├── embeddings.py
│   │   ├── generator.py
│   │   └── retriever.py
│   │
│   ├── api/
│   │   └── chat.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   │
│   ├── ingestion/
│   │   └── ingest.py
│   │
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│   │
│   ├── test_ai.py
│   ├── test_generator.py
│   └── test_search.py
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── knowledge/
│   ├── company.md
│   ├── services.md
│   ├── products.md
│   ├── case_studies.md
│   ├── internships.md
│   ├── jobs.md
│   └── technologies.md
│
└── .gitignore
```

---

# ⚙️ Local Installation

## 1. Clone the Repository

```bash
git clone https://github.com/dayanshkuroliya/cynbit-ai-opportunity-assistant.git
```

```bash
cd cynbit-ai-opportunity-assistant
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the FastAPI server:

```powershell
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

#  Frontend Setup

Open another terminal.

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally run at:

```text
http://localhost:5173
```

---

#  API

## POST `/chat`

The frontend sends a question to the FastAPI backend.

### Request

```json
{
  "question": "What internships does Cynbit offer?"
}
```

### Response

```json
{
  "question": "What internships does Cynbit offer?",
  "answer": "Cynbit offers the following internships...",
  "sources": [
    {
      "file": "internships.md",
      "score": 0.8356
    }
  ]
}
```

---

#  Example Questions

Try asking:

```text
What internships does Cynbit offer?
```

```text
What services does Cynbit provide?
```

```text
What technologies does Cynbit use?
```

```text
What products has Cynbit developed?
```

```text
What AI-related opportunities are available?
```

```text
What kind of projects has Cynbit worked on?
```

---

#  Security

The project is configured to avoid committing sensitive environment files.

The repository ignores:

```text
.env
venv/
node_modules/
__pycache__/
*.pyc
dist/
.vite/
```

API keys or private credentials should never be committed to the repository.

---

#  Future Improvements

The current version is an MVP. Possible improvements include:

- Business / Career conversation modes
- PostgreSQL + pgvector
- Persistent conversation history
- Improved semantic retrieval
- Better answer formatting
- Streaming AI responses
- Website integration as a floating chatbot
- Admin knowledge-base management
- Multilingual support
- Cloud deployment
- Larger production-grade language model
- Analytics for frequently asked questions
- Lead-generation and contact CTAs

---

#  Project Objective

The main objective of this project is to demonstrate how **Retrieval-Augmented Generation (RAG)** can be used to improve information discovery on a technology company's website.

The project combines:

```text
React
   +
FastAPI
   +
Semantic Search
   +
Embeddings
   +
Local LLM
   +
Structured Knowledge Base
```

to create a practical AI-powered website assistant.

---

# Author

**Dayansh Kuroliya**

B.Tech CSE — Artificial Intelligence & Machine Learning

GitHub:

https://github.com/dayanshkuroliya

---

# License

This project is created for educational, portfolio, and internship evaluation purposes.
