import requests
import sqlite3

def get_weather(api_key, cities):
    base = "https://api.openweathermap.org/data/2.5/weather"
    conn = sqlite3.connect("project.db")
    cur = conn.cursor()

    for city in cities:
        params = {
            "appid": api_key,
            "q": city,
            "units": "metric" 
        }

        response = requests.get(base, params=params)
        info = response.json()

        # skip if a city is not found
        if info.get("cod") != 200:
            print("Error for", city, "->", info.get("message"))
            continue

        # The main weather group
        main_group = info["weather"][0]["main"]

        # create weather table
        cur.execute("""
            INSERT INTO Weather (city, main_group)
            VALUES (?, ?)
        """, (city, main_group))

    conn.commit()
    conn.close()
    print("Weather data saved for", len(cities), "cities")

if __name__ == "__main__":
    WEATHER_KEY = "26e29561a104a07614547a0a10d09676"  

    cities = [
        "Ann Arbor", "Detroit", "Chicago", "New York", "Los Angeles",
        "Miami", "Seattle", "Boston", "Houston", "Phoenix"
    ]

    get_weather(WEATHER_KEY, cities)