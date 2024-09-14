from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone as PineconeLangchain
#import pinecone
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)
# print(os.listdir('data'))
extracted_data = load_pdf(r'D:\abdullah_work\Gen-AI\End-to-end-Medical-Chatbot-using-Llama2\data')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()
index_name="medical-bot"


#Initializing the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
# indexes = pc.list_indexes()
# print('indexes_name: ',indexes)
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud='aws',region='us-east-1')
    )
else:
    pass




#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeLangchain.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
