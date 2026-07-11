from app.retriever import create_retriever
from app.vectorstore import load_vectorstore
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

vector_store = load_vectorstore()

retriever = create_retriever(vector_store)

def ask(question):
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

    return response.content


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or 'quit'): ")

        if question.lower() == "quit":
            break

        answer = ask(question)
        print("\nAnswer:")
        print(answer)