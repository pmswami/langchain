from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()


# create fastapi app
app = FastAPI(
    title="LangChain API",
    description="API for LangChain",
    version="0.1.0",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# model = ChatOpenAI()
model = Ollama(model="gemma3:1b")
llm = Ollama(model="deepseek-r1:1.5b")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} around 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} around 150 words")


add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)