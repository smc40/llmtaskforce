import logging

import streamlit as st

import src.utils as utl

logging.basicConfig(level=logging.INFO)
utl.set_page_config(st)


st.markdown('# 🚀 LLM Taskforce Collabathon 2024')

st.markdown('## Goals')

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
font_size = '25px'
fun = outer_template.format(fontsize=font_size, content=f'Having {inner_template.format(color=color, fontsize=font_size, content="FUN")} working together')
learn = outer_template.format(fontsize=font_size, content=f'{inner_template.format(color=color, fontsize=font_size, content="LEARN")} from each other')
home = outer_template.format(fontsize=font_size, content=f'Take something {inner_template.format(color=color, fontsize=font_size, content="HOME")}')


st.markdown(fun, unsafe_allow_html=True)
st.markdown(learn, unsafe_allow_html=True)
st.markdown(home, unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
text = """<hr><p style="font-weight: bold; font-size: 25px">🍲 ROAST MY LLM</p>
<p style="font-size: 20px">Let's expose those LLM weaknesses like hallucinations, inconsistencies, biases, prompt injection etc.</p>
<p>Pitched by: Christoph</p>
<hr>
<p style="font-weight: bold; font-size: 25px">🧪 BENCHMARK YOUR LLM</p>
<p style="font-size: 20px">Let's create and put LLMs to the test.</p>
<p>Pitched by: Dominic</p>
<hr>
<p style="font-weight: bold; font-size: 25px">👾 STANDARDIZED NER</p>
<p style="font-size: 20px">Automate the labelling of reported reactions with a standardized 
medical dictionary (e.g. MedDRA, ICD-10, ICD-11)</p>
<p>Pitched by: Dennis</p>
<hr>
"""
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('## Use Cases')
st.markdown(text, unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.markdown('## Schedule')
st.image('resources/schedule.png', use_column_width=True)
