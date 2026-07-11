# Multi PDF RAG (LangChain)

## Overview
A Retrieval-Augmented Generation (RAG) application built using LangChain, ChromaDB, Gemini Embeddings, and Gemini 2.5 Flash.

## Features
- Load multiple PDFs
- Split into semantic chunks
- Store embeddings in ChromaDB
- Retrieve relevant chunks using vector similarity
- Generate answers grounded in retrieved context

## Tech Stack
- Python
- LangChain
- ChromaDB
- Gemini Embeddings
- Gemini 2.5 Flash

## Project Structure
app/
    loader.py
    splitter.py
    vectorstore.py
    retriever.py
    chat.py
    index.py

## How to Run
1. Install dependencies
2. Add GOOGLE_API_KEY
3. Place PDFs in data/docs
4. Run index.py
5. Run chat.py