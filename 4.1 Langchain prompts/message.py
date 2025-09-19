from langchain.core.prompts import PromptTemplate, SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama



model=ChatOllama(model="mistral:7b")

message=[
    SystemMessage(content='you are a helpful research assistant .'),
    HumanMessage(content="what is AI.")
]

result=model.invoke(message)
message.append(AIMessage(content=result.content))

print(message)