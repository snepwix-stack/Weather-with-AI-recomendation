from http.client import responses

import requests
import google.generativeai as genai

#weather api key
WEATHER_KEY = ""

#gemini key
GEMINI_KEY = ""
#your city
CITY = input("City: ")

genai.configure(api_key=GEMINI_KEY)
#ai model https://aistudio.google.com/
model = genai.GenerativeModel("gemini-3-flash-preview")

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Weather in {CITY}: {temp}°C, {desc}"
    elif response.status_code == 401:
        return "ERROR_401"
    else:
        return f"Error API: {response.status_code}"

def ask_gemini(info):
    #promt = Your promt
    promt = f"{info}{CITY}"
    response = model.generate_content(promt)
    return response.text

weather_info = get_weather()

if weather_info == "ERROR_401":
    print("API_Error")
else:
    print(f"✅ Data received: {weather_info}")
    print("🤖 Gemini generting answer...")
    advice = ask_gemini(weather_info)
    print("-" * 40)
    print(advice)
