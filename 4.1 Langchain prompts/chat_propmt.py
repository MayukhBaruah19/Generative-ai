from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ("system", "You are a helpful AI assistant that specializes in {domin}."),
    ("human", "Explain the concept of {topic} in a {style} manner.")
])


prompt=chat_template.invoke(
    {
        "domin": "science",
        "topic": "quantum mechanics",
        "style": "simple"
    }
)

print(prompt)
