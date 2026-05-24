import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)  # ask the API for data

data = response.json()  # convert it to a dictionary

print(data["name"])    # pikachu
print(data["height"])  # 4
print(data["weight"])  # 60