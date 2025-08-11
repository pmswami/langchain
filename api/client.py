import requests
import streamlit as st

def get_openai_response(input_text):

    response = requests.post(
        url = "http://localhost:8000/essay/invoke",
        json={"input":{"topic":input_text}},
        )
    return response.json()["output"]


def get_ollama_response(input_text):

    response = requests.post(
        url = "http://localhost:8000/poem/invoke",
        json={"input":{"topic":input_text}},
        )
    return response.json()["output"]


st.title("Demo of OpenAI and Ollama models")
input_text = st.text_input("Write essay: ")
input_text1 = st.text_input("Write poem: ")

if input_text:
    st.write("Essay: ", get_openai_response(input_text))

if input_text1:
    st.write("Essay: ", get_ollama_response(input_text1))
    