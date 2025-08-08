from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
import os
import streamlit as st
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
# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOllama(model="deepseek-r1:1.5b") # open sourced model
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))