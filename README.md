# Multi PDF RAG (LangChain)

## Overview
A Retrieval-Augmented Generation (RAG) application built with LangChain, ChromaDB, Gemini Embeddings, and Gemini 2.5 Flash. The application indexes multiple PDF documents into a persistent Chroma vector database and answers user questions using retrieval-augmented generation.

## Features
- Load multiple PDF documents
- Split documents into overlapping semantic chunks
- Generate embeddings with Gemini
- Store embeddings in a persistent ChromaDB vector store
- Retrieve the most relevant chunks using vector similarity search
- Generate answers grounded in retrieved context

## Tech Stack
- Python
- LangChain
- ChromaDB
- Gemini Embeddings
- Gemini 2.5 Flash

## Project Structure

```
app/
├── loader.py        # Load PDFs into LangChain Documents
├── splitter.py      # Split Documents into chunks
├── vectorstore.py   # Create and persist Chroma vector store
├── retriever.py     # Load vector store and create retriever
├── chat.py          # Retrieve context and generate answers
├── index.py         # Build the vector database

data/
├── docs/            # Input PDFs
└── chroma/          # Persistent Chroma database
```

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create a `.env` file

```text
GOOGLE_API_KEY=your_api_key
```

3. Add PDF files to:

```
data/docs/
```

4. Index the documents (only required when adding or updating PDFs)

```bash
python app/index.py
```

5. Start the chatbot

```bash
python app/chat.py
```

## RAG Pipeline

```
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
Prompt
   ↓
Gemini 2.5 Flash
   ↓
Answer
```

Note: The vector database only needs to be rebuilt when PDFs are added or modified. During chat, 
the application loads the existing Chroma database and performs retrieval without reprocessing the documents.