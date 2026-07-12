# Multi PDF RAG (LangChain)

## Overview

A Retrieval-Augmented Generation (RAG) API built with FastAPI, LangChain, ChromaDB, Gemini Embeddings, and Gemini 2.5 Flash.
The application indexes multiple PDF documents into a persistent Chroma vector database and exposes a REST API for answering 
user questions using retrieval-augmented generation.

## Features

* Load multiple PDF documents
* Split documents into overlapping semantic chunks
* Generate embeddings using Gemini
* Store embeddings in a persistent ChromaDB vector database
* Retrieve relevant chunks using vector similarity search
* Generate answers grounded in retrieved context
* Expose a REST API with FastAPI

## Tech Stack

* Python
* FastAPI
* LangChain
* ChromaDB
* Gemini Embeddings
* Gemini 2.5 Flash

## Project Structure

```text
app/
├── loader.py        # Load PDFs into LangChain Documents
├── splitter.py      # Split Documents into chunks
├── vectorstore.py   # Create and persist Chroma vector store
├── retriever.py     # Load vector store and create retriever
├── chat.py          # Retrieve context and generate answers
├── index.py         # Build the vector database
├── main.py          # FastAPI application

data/
├── docs/            # Input PDFs
└── chroma/          # Persistent Chroma database
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file

```text
GOOGLE_API_KEY=your_api_key
```

### 3. Add PDF documents

Place your PDF files inside:

```text
data/docs/
```

### 4. Build the vector database

Run this only when adding or modifying PDFs.

```bash
python app/index.py
```

### 5. Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Health Check

**GET /**

Response:

```json
{
  "message": "RAG API is running"
}
```

---

### Ask a Question

**POST /chat**

Request:

```json
{
  "question": "What is self attention?"
}
```

Example Response:

```json
{
  "answer": "Self-attention is a mechanism that allows each token in a sequence to attend to every other token..."
}
```

## RAG Pipeline

```text
PDFs
   ↓
Loader
   ↓
Documents
   ↓
Text Splitter
   ↓
Chunks
   ↓
Gemini Embeddings
   ↓
ChromaDB
   ↓
Retriever
   ↓
Prompt Template
   ↓
Gemini 2.5 Flash
   ↓
Answer
```

## Notes

* The vector database only needs to be rebuilt when PDFs are added or modified.
* During inference, the application loads the existing Chroma database and performs retrieval without reprocessing the PDFs.
* Chroma automatically uses the configured embedding model to embed user queries during similarity search.
