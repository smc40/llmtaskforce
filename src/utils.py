from dotenv import load_dotenv
import logging
import os
from typing import List

from openai import AzureOpenAI, OpenAIError

from src.settings import CHATBOT_SYSTEM_MSG

load_dotenv()

try:
    _CLIENT = AzureOpenAI(
      azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
      api_key=os.getenv("AZURE_OPENAI_API_KEY"),
      api_version="2024-02-01"
    )
except OpenAIError as e:
    logging.error(e)


def get_chatgpt_response(messages: List[dict], model: str):
    response = _CLIENT.chat.completions.create(
        model=model,
        messages=messages
    )
    content = response.choices[0].message.content
    return content


def get_initial_chatbot_messages() -> List[dict]:
    messages = [{'role': 'system', 'content': CHATBOT_SYSTEM_MSG}]
    return messages


def set_page_config(st):
    st.set_page_config(page_title='LLM Taskforce',
                       page_icon="ℹ️",
                       # layout='wide',
                       )


def update_chat(messages: List[dict], role: str, content: str) -> List[dict]:
    messages.append({"role": role, "content": content})
    return messages

