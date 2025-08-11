import requests
from dotenv import load_dotenv #external library to load environment variables
import os
from pprint import pprint

load_dotenv()  # Load environment variables from .env file
print(os.getenv("API_KEY"))
def get_current_weather( ):
    print("Getting current weather...")

    city=input("\n Enter city name:  \n")



    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    
    #print(request_url)
    weather_data=requests.get(request_url).json()
    pprint(weather_data)

get_current_weather()
