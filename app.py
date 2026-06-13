# =========================
# STEP 1: Install libraries
# =========================
!pip install requests matplotlib

# =========================
# STEP 2: Imports
# =========================
import requests
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt

# =========================
# STEP 3: API KEY
# =========================
API_KEY = "26ee765f5e6c78c3bb15d2b6d4fad140"

# =========================
# STEP 4: GUI ELEMENTS
# =========================
title = widgets.HTML("<h2>Weather Forecasting App (Fixed Version)</h2>")

single_city = widgets.Text(
    placeholder="Enter single city",
    description="City:"
)

multi_city = widgets.Text(
    placeholder="Mumbai, Delhi, Pune",
    description="Cities:"
)

btn_single = widgets.Button(description="Get Weather", button_style="primary")
btn_multi = widgets.Button(description="Compare Cities", button_style="success")

output = widgets.Output()

# =========================
# STEP 5: FUNCTION TO GET WEATHER
# =========================
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()

    if data.get("cod") != 200:
        return None

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind": data["wind"]["speed"]
    }

# =========================
# STEP 6: SINGLE CITY
# =========================
def show_single(b):
    with output:
        clear_output()

        city = single_city.value.strip()
        data = get_weather(city)

        if not data:
            print(" City not found")
            return

        print("🌦️ WEATHER REPORT")
        print("------------------")
        print("City:", data["city"])
        print("Temperature:", data["temp"], "°C")
        print("Weather:", data["weather"])
        print("Humidity:", data["humidity"], "%")
        print("Wind:", data["wind"], "m/s")

btn_single.on_click(show_single)

# =========================
# STEP 7: MULTI CITY COMPARISON (FIXED)
# =========================
def show_multi(b):
    with output:
        clear_output()

        cities = [c.strip() for c in multi_city.value.split(",") if c.strip()]

        if len(cities) == 0:
            print("⚠️ Please enter at least one city")
            return

        city_names = []
        temps = []

        for city in cities:
            data = get_weather(city)

            if data:
                city_names.append(data["city"])
                temps.append(data["temp"])

        if len(city_names) == 0:
            print(" No valid cities found")
            return

        # PRINT TABLE
        print(" CITY COMPARISON")
        print("--------------------")

        for i in range(len(city_names)):
            print(f"{city_names[i]} : {temps[i]} °C")

        # PLOT GRAPH (FIXED)
        plt.figure(figsize=(6,4))
        plt.bar(city_names, temps, color="orange")
        plt.title("Temperature Comparison Between Cities")
        plt.xlabel("Cities")
        plt.ylabel("Temperature (°C)")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.show()

btn_multi.on_click(show_multi)

# =========================
# STEP 8: DISPLAY UI
# =========================
display(title)
display(single_city, btn_single)
display(multi_city, btn_multi)
display(output)
