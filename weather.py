import requests
from settings import API_KEY, BASE_URL


def get_weather(city):

    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        weather = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "time": data["location"]["localtime"],
            "temperature": data["current"]["temp_c"],
            "feels_like": data["current"]["feelslike_c"],
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"],
            "wind": data["current"]["wind_kph"],
            "uv": data["current"]["uv"],
            "rain": data["current"]["chance_of_rain"]
        } 

        return weather

    except Exception as e:
        print(e)
        return None