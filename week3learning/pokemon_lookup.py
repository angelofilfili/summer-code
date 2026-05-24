import requests

while True:

    input_name = input("Please provide a pokemon name: ")

    try:
        response = requests.get('https://pokeapi.co/api/v2/pokemon/' + input_name)
        if response.status_code == 404:
            raise Exception()
        data = response.json()
        print(data["name"])    
        print(data["height"])  
        print(data["weight"])
        stat_list = data['stats']
        for s in stat_list:
            stat = s['base_stat']
            stat_name = s['stat']['name']
            print(stat_name + ":", stat)
        type_list = data["types"]
        for s in type_list:
            name_type = s['type']['name']
            print("Type:", name_type)
        break

    except:
        print("Pokemon not found!")
        print("Try again!")
