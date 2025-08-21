from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

llm=ChatOllama(
    model='llama3.2:1b',
    base_url='http://localhost:11434',
    temperature=0.7
)

prompt=ChatPromptTemplate.from_messages(
    """
   Answer the following question based only on the provided context:
    <context>   
    {context}
    </context>
"""
)

document_chain=create_stuff_document_chain( llm, prompt)
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="Python is a programming language created by Guido van Rossum."),
    Document(page_content="It is widely used in data science, machine learning, and web development.")
]

# Create the chain
document_chain = create_stuff_document_chain(llm, prompt)

# Invoke the chain with documents
response = document_chain.invoke({"context": docs})

print(response)
