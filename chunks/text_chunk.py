from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextChunk():
    def chunks(self,texts):
        text_spliter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 100)
        text_chunk = text_spliter.split_documents(texts)
        return text_chunk

chunks = TextChunk()