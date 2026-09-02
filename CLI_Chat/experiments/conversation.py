import urllib.request
import json
import urllib.error
import json.decoder

url = 'http://localhost:11434/api/chat'

messages = []

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
    'stream':True,
    "options":{
        "temperature":0.8,
        "top_p":0.5
    }
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
            for line in response:
                chunk = json.loads(line.decode('utf-8'))
                if chunk['done']:
                    break
                print(f"{chunk['message']['content']}", end="", flush=True)
            print()
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
