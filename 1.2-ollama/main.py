import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate 
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Define expert system prompt for subjects from class 6 to 10
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", 
         "You are an expert tutor with deep knowledge in all subjects taught in grades 6 to 10, including science, mathematics, social studies, English, and computer science. "
         "You explain clearly, help students understand complex ideas, and respond with patience and examples appropriate to their level."),
        ("user", "Question: {question}")
    ]
)

# Set up the LLM and parser
llm = Ollama(model="llama3.2:1b")
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

# Streamlit interface
st.title("📚 School Subjects Expert Chatbot (Grades 6–10)")
input_text = st.text_input('Ask a question from any subject (Grades 6 to 10):')

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
