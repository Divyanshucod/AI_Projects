import urllib.request
import json
import urllib.error
import json.decoder

class llmClient:
    def __init__(self, model='mistral:7b', url='http://localhost:11434/api/chat'):
        self.model = model
        self.url = url
    def chat(self, messages, temperature=0.5, top_p=0.8):
        payload = {
            "model": "mistral:7b",
            "messages": messages,
            'stream':False,
            "options":{
                "temperature":temperature,
                "top_p":top_p
            }
        }
        data = json.dumps(payload).encode("utf-8")
        
        request = urllib.request.Request(
                self.url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST"
        )
        with urllib.request.urlopen(request) as response:
           result = json.loads(response.read().decode('utf-8'))
        return result['message']['content']
    def steam(self, messages, temperature=0.5, top_p=0.8):
            payload = {
                "model": "mistral:7b",
                "messages": messages,
                'stream':True,
                "options":{
                    "temperature":temperature,
                    "top_p":top_p
                }
            }
            data = json.dumps(payload).encode("utf-8")
            
            request = urllib.request.Request(
                    self.url,
                    data=data,
                    headers={"Content-Type": "application/json"},
                    method="POST"
            )
            with urllib.request.urlopen(request) as response:
                for line in response:
                     chunk = json.loads(line.decode('utf-8'))
                     if chunk.get('done'):
                          break
                     yield chunk['message']['content']


