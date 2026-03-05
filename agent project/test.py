from langchain_core.runnables import RunnableLambda
from vector_base import vector_store
import pandas as pd
city_name='南宁市'
vs=vector_store()
def fdoc(docs):
            str=''
            if not  docs:
                return '无'
            else:
                for i in docs:
                    str+=f'{i.page_content},{i.metadata}'
                return str
ret=vs.get_retriever()
chain=RunnableLambda(lambda x:city_name)|ret|fdoc
print(chain.invoke(city_name))