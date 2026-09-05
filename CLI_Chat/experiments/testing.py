from Client import llmClient


client = llmClient()
messages = [
    {'role':'user',
    'content':"Hi!"}
]
print(client.chat(messages))

# ## with stream
# for chunk in client.steam(messages):
#     print(chunk, end="", flush=True)