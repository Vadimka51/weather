import requests


user_city = input('Введите город: ')
url = f"https://wttr.in/{user_city}?ru"

params = {
    "n" : '',
    "m" : '',
    "ru": '',
    "1" : ''
}

response = requests.get(url, params = params)
response.raise_for_status()
print(response.text)