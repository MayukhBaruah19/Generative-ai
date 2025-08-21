import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## prompt templets
promptemplets=ChatPromptTemplate.from_messages(
    [
        ("system","you ar an AI engineer. provide me answers based on the questions"),
        ("user","Question:{question}")
    ]

)

#streamlit app
st.title("An chatbot using llama3 using langchain")
input_text=st.text_input('What Question in your mind')

llm=Ollama(model="deepseek-r1:1.5b")
output_parser=StrOutputParser()
chain=promptemplets|llm|output_parser

if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)