from langchain_huggingface import HuggingFaceEmbeddings

class ChunkEmbeddings():
    def chunk_embeddings(self):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return embeddings
chunkss_embeddding = ChunkEmbeddings()