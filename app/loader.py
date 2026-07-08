from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = Path(__file__).resolve().parent.parent



def load_documents():
    docs_dir = BASE_DIR / "data" / "docs"

    all_documents = []

    for pdf in docs_dir.glob("*.pdf"):
        # Create a loader object for the current PDF.
        loader = PyPDFLoader(pdf)

        # Read the PDF and return a list of Document objects
        # (one Document per page).
        documents = loader.load()

        # Combine pages from all PDFs into a single list.
        all_documents.extend(documents)

    return all_documents



# Input:
# PDF files
#
# Output:
# list[Document]
#
# Uses:
# PyPDFLoader