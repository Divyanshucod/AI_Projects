import json
import urllib.request
import urllib.error

url = "http://localhost:11434/api/generate"

payload = {
    "model": "mistral:7b",
    "prompt": "What is an NPC?",
    "stream": False
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
    print(result)
except urllib.error.HTTPError as e:
    error_body = e.read().decode("utf-8")
    print(f"HTTP error: {error_body}")
    raise

except urllib.error.URLError as e:
    print(f"Connection error: {e.reason}")
    raise