from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


# Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfull assistant. Please respond to queries in english only"),
        ("user", "Question:{question}")
    ]
)


# streamlit framework
st.title("Demo")
input_text = st.text_input("Search")


#Create chain
llm = Ollama(model="gemma3:1b") # open sourced model
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))