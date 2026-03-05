import pandas as pd
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import config
df = pd.read_excel('.//agent project//AMap_adcode_citycode.xlsx',names=['city_name','city_id'])
spliter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100,separators=['\n'],length_function=len)
vector_store=Chroma(collection_name=config.cname,embedding_function=config.em,persist_directory=config.dpath)
chunks=spliter.split_text(df.to_string())
vector_store.add_texts(chunks,metadata=[{'source':f'AMap_adcode_citycode.xlsx'}]*len(chunks))

