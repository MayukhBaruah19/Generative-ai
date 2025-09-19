
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt=ChatPromptTemplate(
    [
        ('system', 'You are a helpful assistant.'),
        ('human', 'Question: {question}')
    ]
)

st.title("langchain demo app")
input_question=st.text_input("Enter your question here")

llm=ChatOllama(model='mistral:7b')
output=StrOutputParser()
chain=prompt | llm | output
if input_question:
    response=chain.invoke({"question": input_question})
    st.write(response)