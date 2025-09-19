from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support assistant.'),
    MessagesPlaceholder(variable_name='Chat_history'),
    ('human','{query}')
])


# load chat history
chat_history=[]
with open ('chat_history.txt') as f:
    chat_history.extend( f.readlines())
print(chat_history)

#chat prompt
prompt=chat_template.invoke({
    'Chat_history':chat_history,
    'query':'How to use langchain?'
    })

print(prompt)