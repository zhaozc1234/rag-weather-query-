from langchain_chroma import Chroma
import config
class vector_store(object):
    def __init__(self):
        self.embedding=config.em
        self.vectorstore=Chroma(collection_name=config.cname,embedding_function=self.embedding,persist_directory=config.dpath)
    def get_retriever(self):
        return self.vectorstore.as_retriever(search_kwargs={'k':config.k})