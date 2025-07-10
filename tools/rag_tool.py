from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as PineconeStore
from langchain.chains import RetrievalQA
import pinecone
import os

# --- 1. Initialisation Pinecone
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")  # ex: "gcp-starter"
)

index_name = "prevoyance"
index = pinecone.Index(index_name)

# --- 2. Création du vector store LangChain
embedding_model = OpenAIEmbeddings()
vectorstore = PineconeStore(index, embedding_model, "text")

# --- 3. Création du retriever + QA chain
retriever = vectorstore.as_retriever(search_type="similarity", k=3)

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o"),
    retriever=retriever,
    return_source_documents=False
)

# --- 4. Tool utilisable dans LangChain
@tool
def search_rag(query: str) -> str:
    """
    Recherche une information dans la base documentaire prévoyance/assurance.
    """
    print(f"[DEBUG][RAG] search_rag appelé avec la requête : {query}")
    return qa_chain.run(query)