import logging

import streamlit as st

import src.utils as utl

logging.basicConfig(level=logging.INFO)
utl.set_page_config(st)


st.markdown('## LLM Taskforce Collabathon 2024')

st.markdown('### Goals')

outer_template = """<p style="border-radius: 15px; 
box-shadow: 2px 2px 4px #a0a0a0; 
color: grey; 
font-weight: bold; 
border: 2px solid #505050; 
padding: 20px;
text-align: left;
font-size: {fontsize}">
{content}
</p>
"""

inner_template = """<span style="border-radius: 15px; 
color: white; 
font-weight: bold; 
background-color: {color}; 
padding: 10px;
text-align: center;
font-size: {fontsize}">
{content}
</span>
"""

# color = '#2FD072'
color = '#2878D7'
font_size = '30px'
fun = outer_template.format(fontsize=font_size, content=f'Having {inner_template.format(color=color, fontsize=font_size, content="FUN")} working together')
learn = outer_template.format(fontsize=font_size, content=f'{inner_template.format(color=color, fontsize=font_size, content="LEARN")} from each other')
home = outer_template.format(fontsize=font_size, content=f'Take something {inner_template.format(color=color, fontsize=font_size, content="HOME")}')

st.markdown(fun, unsafe_allow_html=True)
st.markdown(learn, unsafe_allow_html=True)
st.markdown(home, unsafe_allow_html=True)


st.markdown('### Schedule')
st.image('resources/schedule.png')
