from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = Path(__file__).resolve().parent.parent

def load_documents():
    docs_dir = BASE_DIR / "data" / "docs"

    all_documents = []

    for pdf in docs_dir.glob("*.pdf"):
        loader = PyPDFLoader(pdf)
        documents = loader.load()

        all_documents.extend(documents)

    return all_documents


