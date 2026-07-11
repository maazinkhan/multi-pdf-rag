from app.retriever import create_retriever
from app.vectorstore import load_vectorstore
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# This does not recreate embeddings.It does not read PDFs.
# It simply says: "Open my existing Chroma database from disk."
vector_store = load_vectorstore()

#Convert vectorstore into a retriever
#This creates a higher-level search interface.
retriever = create_retriever(vector_store)

question = input("Ask a question: ")

docs = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in docs
)


prompt = ChatPromptTemplate.from_template(
    """
    Answer the question using only the context below.

    Context:
    {context}

    Question:
    {question}
    """
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

messages = prompt.invoke(
    {
        "context": context,
        "question": question
    }
)

response = llm.invoke(messages)

print(response.content)