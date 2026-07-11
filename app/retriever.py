from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from pathlib import Path
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def create_retriever(vector_store):
    retriever = vector_store.as_retriever(
        search_kwargs={"k":4}
    )

    return retriever