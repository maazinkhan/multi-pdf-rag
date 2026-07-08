from langchain_text_splitters import RecursiveCharacterTextSplitter



def split_documents(documents):
    """
        Split LangChain Document objects into smaller chunks while
        preserving metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

# Input:
# list[Document]
#
# Output:
# list[Document] (smaller chunks)
#
# Uses:
# RecursiveCharacterTextSplitter
#
# Metadata:
# Preserved automatically