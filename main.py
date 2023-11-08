import requests

url = "https://wttr.in/москва"

response = requests.get(url)
response.raise_for_status()
print(response.text)