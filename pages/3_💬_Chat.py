import streamlit as st

import src.utils as utl

utl.set_page_config(st)

if 'messages' not in st.session_state:
    st.session_state['messages'] = utl.get_initial_chatbot_messages()


st.markdown("### If the 👸 isn't listening, talk to the ✋")
col1, col2 = st.columns([1, 2])
with col1:
    model = st.selectbox('Model', options=['gpt-35-turbo', 'gpt-4'])
    if st.button('clear'):
        st.session_state['messages'] = utl.get_initial_chatbot_messages()


for message in st.session_state['messages']:
    role = message['role']
    if role in ['user', 'assistant']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

prompt = st.chat_input("Wazzup?")

if prompt and model:
    messages = st.session_state['messages']

    with st.chat_message('user'):
        st.markdown(prompt)
    messages = utl.update_chat(messages, "user", prompt)

    with st.spinner("generating..."):
        response = utl.get_chatgpt_response(messages, model)

    with st.chat_message('assistant'):
        st.markdown(response)
    utl.update_chat(messages, "assistant", response)

