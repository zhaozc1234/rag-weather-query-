from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
import config
from vector_base import vector_store
from langchain_core.runnables import RunnableLambda
import requests
vs=vector_store()
@tool(description='城市代码')
def get_id(str):
      '''根据城市名称查询城市代码'''
      def fdoc(docs):
            str=''
            if not  docs:
                return '无'
            else:
                for i in docs:
                    str+=f'{i.page_content},{i.metadata}'
                return str
      ret=vs.get_retriever()
      chain=RunnableLambda(lambda x:str)|ret|fdoc
      return chain.invoke(str)
@tool(description='查询天气')
def get_weather(id):
      '''根据城市代码查询天气'''
      url=f'https://restapi.amap.com/v3/weather/weatherInfo?city={id}&key=a287a7c3e771efba210f87d8020cff37&extensions=base'
      resp=requests.get(url)
      if resp.status_code==200:
         resp1=resp.json()
         resp2=resp1['lives']
         return resp2
      else:
        return '无'
class ag :
    def __init__(self):
        self.agent=create_agent(
            model=ChatTongyi(model='qwen3-max'),
            tools=[get_id, get_weather],
            system_prompt='你是一个聊天助手，你可通过工具查询城市代码，找到最合适的一个城市代码后通过调用工具查询天气,同时，只输出一个地方的天气信息，不要输出其他内容'
        )
  
    def speak(self,str):
        res=self.agent.invoke({'messages':[{'role':'user','content':str}]},stream_mode='values')
        return res['messages'][-1].content
