from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
import glob

def setup_vector_db():
    # Find the correct datasets directory (works with both protocol/ and protocol-public/)
    datasets_paths = glob.glob("..*/datasets/")
    if not datasets_paths:
        raise FileNotFoundError("Could not find datasets directory")
    
    # Use the first found datasets directory
    datasets_path = datasets_paths[0]
    
    # Load all markdown files from datasets directory
    loader = DirectoryLoader(datasets_path, glob="**/*.md")
    documents = loader.load()
    
    # Create vector store
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory="./vector_db"
    )
    
    # Add documents to vector store
    vectorstore.add_documents(documents)
    vectorstore.persist() 