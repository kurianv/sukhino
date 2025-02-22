import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os
import datetime
load_dotenv()

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("user_response")
collection.upsert(
    documents = [],
    ids = [],
    embeddings=[]

)

document_history = {}

def embedding(response):
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key = os.getenv("OPENAI_API_KEY"),
        model_name = "text-embedding-3-small",  
    )
    embed = openai_ef(response)

    return embed

def update(ids, response):
    for i, doc_id in enumerate(ids):
        if doc_id not in document_history:
            document_history[doc_id] = []
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        document_history[doc_id].append({
            "timestamp": [timestamp],
            "document": [response],
            "embedding": [embedding(response)]
        })
        
        # Perform the upsert operation
        collection.upsert(
            documents=[response],
            ids=[doc_id],
            embeddings=[embedding(response)]
        )
    
    









