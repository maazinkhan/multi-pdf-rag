from app.loader import load_documents
from app.splitter import split_documents
from app.vectorstore import create_vectorstore

documents = load_documents()

chunks = split_documents(documents)

print(f"Loaded {len(documents)} pages")
print(f"Created {len(chunks)} chunks")

vector_store = create_vectorstore(chunks) #-- This is already run once and has created chromdb in the path

print(vector_store)
