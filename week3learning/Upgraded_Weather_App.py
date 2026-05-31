from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

api_key = os.getenv("API_KEY")

try:
    with open("last_city.txt", "r") as f:
        last_city = f.read()
    print("Last searched city:", last_city)
except:
    last_city = ""

while True:

    if last_city == "":
        city_name = input("\nName a city (enter Q to quit): ")
    else:
        city_name = input(f"\nName a city (enter Q to quit, default: {last_city}): ")

    if city_name == "":
        city_name = last_city

    if city_name == "Q":
        break

    temp_value = input("Do you want Celsius or Fahrenheit (C or F)? : ")

    if temp_value == "C":
        unit_value = "metric"
    elif temp_value == "F":
        unit_value = "imperial"
    else:
        print("You did not give F or C as a respone for celsius or fahrenheit.")
        print("Try again!")
        continue

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={unit_value}")
        if response.status_code == 404:
            raise Exception()
        data = response.json()
        print("\nCountry:", data['sys']['country'])
        print("Coordinates:", "lon:", data["coord"]["lon"], "lat:", data["coord"]["lat"])
        print("Temperature:", data["main"]["temp"], temp_value)
        print("Feels like:", data["main"]["feels_like"], temp_value)
        print("Humidity:", data["main"]["humidity"], "%")

        description = data["weather"][0]["description"]
        print("Weather Description:", description)

        #print(json.dumps(data, indent=2)) # this shows the whole dictionary but in a clean way to read

        with open("last_city.txt", "w") as f:
            f.write(city_name)

        last_city = city_name

        response2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={unit_value}")
        if response2.status_code == 404:
            raise Exception()
        data2 = response2.json()

        print("\n5 Day Forecast!")

        for entry in data2["list"]:
            if "12:00:00" in entry["dt_txt"]:
                print()
                print("Date:", entry["dt_txt"][:10]) 
                print("Temperature:", entry["main"]["temp"], temp_value)
                print("Weather Description", entry["weather"][0]["description"])
       # print(json.dumps(data2["list"][0], indent=2))

    except:
        print("City doesn't exist!")
        print("Try again!")

    




                            

