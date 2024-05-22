import os

from dotenv import load_dotenv
import streamlit as st

import src.utils as utl

load_dotenv()
utl.set_page_config(st)

st.markdown('### API Keys')

st.markdown('Define environment variables')
code = f"""# Azure OpenAI Variables
export AZURE_OPENAI_API_KEY={os.getenv("AZURE_OPENAI_API_KEY", default='<CHANGEME>')}
export AZURE_OPENAI_ENDPOINT={os.getenv("AZURE_OPENAI_ENDPOINT", default='<CHANGEME>')}
"""
st.code(code, language='bash')

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
