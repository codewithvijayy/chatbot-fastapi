from pinecone import Pinecone ,ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os


class EmbeddingStore():


    def upload_embeddings_to_database(self,ind_name,text_chunk,embeddings):
        pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
        try:
            if ind_name not in pc.list_indexes():
                pc.create_index(
                name=ind_name,
                dimension=384, 
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                ) 
                )
        except Exception as e:
            if "ALREADY_SOURCE" in str(e):
                print(f"index_already created {ind_name} contineous...")
            else:
                raise
        PineconeVectorStore.from_documents(documents=text_chunk,embedding=embeddings,index_name=ind_name)
embedding_store = EmbeddingStore()

