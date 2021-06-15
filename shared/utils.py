import requests
from telegram import Bot

from shared.static import TelegramAPI
from shared.static import WeatherAPI


def get_bot():
    return Bot(TelegramAPI.BOT_API_KEY)


def ping_telegram(message):
    # print(message)
    return get_bot().send_message(TelegramAPI.CHAT_ID, message)


def get_peckham_weather_emoji():
    try:
        weather_id = requests.get(
            WeatherAPI.WEATHER_URL, params={"q": "Peckham", "appid": WeatherAPI.API_KEY}
        ).json()["weather"][0]["id"]
        return WeatherAPI.ID_TO_EMOJI[weather_id]
    except:
        return "🌞"
