import urllib.request
import json
import urllib.error
import json.decoder
import time
# Error handling
class LLMError(Exception):
     pass
class LLMConnectionError(Exception):
     pass
class LLMModelError(Exception):
     pass
class LLMRequestError(Exception):
     pass
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
        start = time.perf_counter()
        with urllib.request.urlopen(request) as response:
           result = json.loads(response.read().decode('utf-8'))
           latency = time.perf_counter() - start
        metadata = {
        "model": result.get("model"),
        "input_tokens": result.get("prompt_eval_count"),
        "output_tokens": result.get("eval_count"),
        "latency": latency,
        }
        return {
            "content": result["message"]["content"],
            "metadata": metadata
        }
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