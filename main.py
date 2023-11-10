import requests


user_city = input('Введите город: ')
url = f"https://wttr.in/{user_city}"

params = {
    "nm1" : '',
    "lang": 'ru',
    
}

response = requests.get(url, params = params)
response.raise_for_status()
print(response.text)