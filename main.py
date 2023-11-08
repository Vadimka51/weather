import requests


user_city = input('Введите город: ')
url = f"https://wttr.in/{user_city}"


response = requests.get(url)
response.raise_for_status()
print(response.text)