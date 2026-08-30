import urllib.request
import json
import urllib.error
import json.decoder

url = 'http://localhost:11434/api/chat'

messages = [
    {
        "role": "system",
        "content": "You are a grumpy medieval blacksmith. Stay in character."
    }
]

while True:
    input_prompt = input('You:')

    if input_prompt.lower() == 'quit':
        break
    messages.append({
        'role':'user',
        'content':input_prompt
    })
    payload = {
    "model": "mistral:7b",
    "messages": messages,
    'stream':False
    }
    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))
        print(f"{result['message']['role']} : {result['message']['content']}")
        messages.append(result['message'])

        # print('Debugging:')
        # print(messages)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"HTTP error: {error_body}")
        raise

    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
        raise
    except json.decoder.JSONDecodeError as e:
        print(f"Invalid JSON response: {e}")
        raise
