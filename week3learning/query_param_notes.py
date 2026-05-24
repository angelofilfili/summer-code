'''Status Codes:
Tells you wether calling an API worked or not by giving a number.

200 = success, data came back fine

404 = not found, whatever you asked for doesn't exist

You can check status code like this:

response = requests.get(url)

if response.status_code == 200
    data = response.json()
    print(data['name'])
else:
    print("Something went wrong:", response.status_code)'''

'''
Query Parameters:
Instead of putting everything in the URL, some APIs let you pass extra 
options using params={}. It's just a dictionary you pass into requests.get()

params = {
    'limit': 5
}

response = requests.get("https://pokeapi.co/api/v2/pokemon", params=params)

This gives use a URL behind the scenes which only gives me 5 results.
https://pokeapi.co/api/v2/pokemon?limit=5

'''

# Putting it all together :

import requests

params = {"limit": 5}

response = requests.get("https://pokeapi.co/api/v2/pokemon", params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)