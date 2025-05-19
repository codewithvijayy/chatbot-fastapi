from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

class PdfLoaders():
    def load_pdf(self,file):
        loader = DirectoryLoader(glob="*.pdf",loader_cls=PyPDFLoader,path=file)
        document = loader.load()
        return document
extract_data_fromPDf = PdfLoaders()