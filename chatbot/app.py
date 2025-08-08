from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "no_key_found")
os.environ["LANGCHAIN_TRACING_V2"] = "true" #for langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "no_key_found")
os.environ["LANGSMITH_TRACING"]="true"
# os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]="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"
os.environ["LANGSMITH_PROJECT"]="PilotProject"

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
llm = ChatOllama(model="deepseek-r1:1.5b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))