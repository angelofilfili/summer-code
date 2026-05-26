from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

while True:

    city_name = input("\nName a city (enter Q to quit): ")

    if city_name == "Q":
        break

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial")
        if response.status_code == 404:
            raise Exception()
        data = response.json()
        print("\nTemperature:", data["main"]["temp"], "F")
        print("Humidity:", data["main"]["humidity"], "%")


        description = data["weather"][0]["description"]
        print("Weather Description:", description)

    except:
        print("City doesn't exist!")
        print("Try again!")




                            

