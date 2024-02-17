# Import libraries & packages
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper

# Set the title and the description of the app
st.title('🎥 YouTube Video Content Assistant') # setting teh title 
st.write('This app helps you generate titles and scripts for your YouTube videos. It uses OpenAI GP') # setting the description
prompt = st.text_input('Write the topic of your video') # text input box

# Prompt templates are used to define the structure of the prompts that will be used to generate the titles and scripts

title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
) # setting the title template

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
) # setting the script template

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history') # setting the title memory
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history') # setting the script memory

# LLM and chains
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

# Wikipedia API Wrapper
wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(script) 

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)