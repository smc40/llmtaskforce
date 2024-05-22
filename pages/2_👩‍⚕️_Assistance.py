import os

import bcrypt
from dotenv import load_dotenv
import streamlit as st

import src.utils as utl

load_dotenv()
utl.set_page_config(st)

if 'registration' not in st.session_state:
    st.session_state['registration'] = False

if 'azure_openai_api_key' not in st.session_state:
    st.session_state['azure_openai_api_key'] = '*****'

if 'azure_openai_endpoint' not in st.session_state:
    st.session_state['azure_openai_endpoint'] = '*****'


def _registration_is_valid(passwd: str):
    return bcrypt.checkpw(passwd.encode(), os.getenv('PASSWD').encode())


def _do_registration():
    passwd = st.session_state['passwd']
    if _registration_is_valid(passwd=passwd):
        st.session_state['registration'] = True
        st.success('You have successfully authenticated!')
        st.session_state['azure_openai_api_key'] = os.getenv("AZURE_OPENAI_API_KEY", default='<CHANGEME>')
        st.session_state['azure_openai_endpoint'] = os.getenv("AZURE_OPENAI_ENDPOINT", default='<CHANGEME>')
    else:
        st.error('Authentication failed')


st.markdown('# 👩‍⚕️ Some Assistance...')
st.markdown('### API Keys')

st.markdown('Environment variables')
if not st.session_state['registration']:
    with st.popover('Show API Keys'):
        st.text_input(label='Password', key='passwd', type='password', on_change=_do_registration)

if st.session_state['registration']:
    code = f"""# Azure OpenAI Variables
AZURE_OPENAI_API_KEY={st.session_state['azure_openai_api_key']}
AZURE_OPENAI_ENDPOINT={st.session_state['azure_openai_endpoint']}
"""
    st.code(code, language='bash')

st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('### Python Example')
st.text('Install openai package')
st.code('pip install openai', language='bash')

st.text('Use Endpoint')
code = """import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt-4", # model = "gpt-35-turbo" or "gpt-4".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)
"""
st.code(code, language="python")
