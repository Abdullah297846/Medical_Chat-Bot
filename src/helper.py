from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceHubEmbeddings


#Extract data from the PDF
def load_pdf(data):
    try:
        # Ensure data points to a valid directory containing PDF files
        loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader, silent_errors=True, show_progress=True)
        documents = loader.load()
        return documents
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []




#Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks



#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceHubEmbeddings(repo_id='sentence-transformers/all-MiniLM-L6-v2',huggingfacehub_api_token='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')
    return embeddings