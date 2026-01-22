from http.client import responses

import requests
import google.generativeai as genai

WEATHER_KEY = "fc2f45776855270fcc2916b4624b2bd6"
GEMINI_KEY = "AIzaSyACAKkghz5wEfpOzVrwgUKkNTAHjKaqjUI"
CITY = "Semey"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Погода в Семее: {temp}°C, {desc}"
    elif response.status_code == 401:
        return "ERROR_401"
    else:
        return f"Ошибка API: {response.status_code}"

def ask_gemini(info):
    promt = f"Погода сегодня такая: {info}. Напиши очень краткий, но злой совет для жителя города Семей. Будь злым!"
    response = model.generate_content(promt)
    return response.text

weather_info = get_weather()

if weather_info == "ERROR_401":
    print("❌ Погодный ключ еще не проснулся. Серверы OpenWeather его пока не видят.")
    print("Давай подождем 20 минут. Но зато мы проверили — библиотеки стоят!")
else:
    print(f"✅ Данные получены: {weather_info}")
    print("🤖 Gemini генерирует совет...")
    advice = ask_gemini(weather_info)
    print("-" * 40)
    print(advice)