import tkinter as tk
from tkinter import messagebox
from weather import get_weather


class WeatherApp:

    def __init__(self, root):

        self.root = root
        self.root.title("🌦 WeatherWise")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        title = tk.Label(
            root,
            text="🌦 WeatherWise",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Arial", 14), width=25)
        self.city_entry.pack(pady=10)

        search_btn = tk.Button(
            root,
            text="Search",
            font=("Arial", 12),
            command=self.search_weather
        )
        search_btn.pack()

        self.result = tk.Label(
            root,
            text="Enter a city name",
            justify="left",
            font=("Arial", 13)
        )

        self.result.pack(pady=20)

    def recommendation(self, temp, rain):
        if rain > 60:
            return "☔ Carry an umbrella."
        if temp < 15:
            return "🧥 Wear warm clothes."

        elif temp < 28:
            return "😊 Pleasant weather."

        else:
            return "🥤 Stay hydrated and wear light clothes."

    def search_weather(self):

        city = self.city_entry.get().strip()

        if city == "":
            messagebox.showwarning("Warning", "Enter a city name.")
            return

        weather = get_weather(city)

        if weather is None:
            messagebox.showerror("Error", "City not found.")
            return

        text = f"""
📍 {weather['city']}, {weather['country']}

🕒 {weather['time']}

🌡 Temperature : {weather['temperature']} °C

🤗 Feels Like : {weather['feels_like']} °C

☁ Condition : {weather['condition']}

💧 Humidity : {weather['humidity']} %

🌬 Wind Speed : {weather['wind']} km/h

☀ UV Index : {weather['uv']}

☔ Chance of Rain : {weather['rain']} %

💡 {self.recommendation(weather['temperature'], weather['rain'])}
"""

        self.result.config(text=text)