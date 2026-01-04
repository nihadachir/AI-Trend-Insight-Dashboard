import requests

url = "http://127.0.0.1:8000/summarize"
data = {"text": "This is a test text."}

r = requests.post(url, json=data)
print(r.json())
