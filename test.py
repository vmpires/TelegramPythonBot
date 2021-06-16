import requests
import json

url = "https://covid19-brazil-api.vercel.app/api/report/v1"

response = requests.get(url)
content = response.json()

print(content)