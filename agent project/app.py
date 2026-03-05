import streamlit as st
from ag import ag

st.title('weather assistant')
st.divider()
q=st.chat_input('请输入您的问题')
if 'message' not in st.session_state:
    st.session_state['message']=[{'role':'assistant','content':'你好，我是天气助手，有什么我可以帮助你的吗？'}]
if 'rag' not in st.session_state:
    st.session_state['rag']=ag()
for i in st.session_state['message']:
    st.chat_message(i['role']).write(i['content'])
if q:
    st.chat_message('user').write(q)
    a=st.session_state['rag'].speak(q)
    st.session_state['message'].append({'role':'user','content':q})
    st.chat_message('assistant').write(a)
    st.session_state['message'].append({'role':'assistant','content':a})
