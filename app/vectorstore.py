from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_chroma import Chroma
from pathlib import Path


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

BASE_DIR = Path(__file__).resolve().parent.parent

def create_vectorstore(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )

    persist_directory = str(BASE_DIR / "data" / "chroma")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding= embeddings,
        persist_directory= persist_directory
    )

    return vector_store

def load_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )

    persist_directory = str(BASE_DIR / "data" / "chroma")

    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    return vector_store

# Input:
# Chunk Documents
#
# Output:
# Persistent Chroma vector database
#
# Uses:
# GoogleGenerativeAIEmbeddings
# Chroma
#
# Important:
# Chroma calls the embedding model automatically.
# We never call embed_documents() ourselves.