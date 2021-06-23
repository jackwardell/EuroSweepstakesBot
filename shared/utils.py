import requests
from telegram import Bot
from pathlib import Path
from shared.static import TelegramAPI
from shared.static import WeatherAPI, EUROS_BOT_ROOT
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pathlib import Path


def get_bot():
    return Bot(TelegramAPI.BOT_API_KEY)


def ping_telegram(message):
    # print(message)
    return get_bot().send_message(TelegramAPI.CHAT_ID, message)


def ping_telegram_with_image(message, image, reply_to_id):
    # print(message)
    with open(image, 'rb') as jpg:
        return get_bot().send_photo(TelegramAPI.CHAT_ID, jpg, message, reply_to_message_id=reply_to_id)


def get_peckham_weather_emoji():
    try:
        weather_id = requests.get(
            WeatherAPI.WEATHER_URL, params={"q": "Peckham", "appid": WeatherAPI.API_KEY}
        ).json()["weather"][0]["id"]
        return WeatherAPI.ID_TO_EMOJI[weather_id]
    except:
        return "🌞"


def make_spiderman_image_path(text: str) -> Path:
    image_name = f"spiderman-{text}.jpg"
    image_path = EUROS_BOT_ROOT / "assets" / image_name
    return image_path


def write_to_spiderman_image(text: str) -> Path:
    image_path = make_spiderman_image_path(text)

    if image_path.exists():
        return image_path

    spiderman_image = Image.open(str(EUROS_BOT_ROOT / "assets/spiderman.jpg"))
    draw = ImageDraw.Draw(spiderman_image)
    font = ImageFont.truetype(str(EUROS_BOT_ROOT / "assets/OpenSans-Bold.ttf"), 64)
    draw.text((100, 175), text, (0, 0, 0), font=font)
    draw.text((520, 225), text, (0, 0, 0), font=font)

    spiderman_image.save(str(image_path))
    return image_path
