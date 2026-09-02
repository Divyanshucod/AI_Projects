import llmClient


client = llmClient.llmClient()
messages = [
    {'role':'user',
    'content':"Hi!"}
]
print(client.chat(messages))