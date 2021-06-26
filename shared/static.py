import os
from pathlib import Path

from dotenv import load_dotenv

EUROS_BOT_ROOT = Path(__file__).resolve().parent.parent

TEAMS_DATA_PATH = EUROS_BOT_ROOT / "data/teams.json"

load_dotenv(EUROS_BOT_ROOT / ".env")


class FootballAPI:
    LEAGUE_ID = "4"
    SEASON = "2020"
    FIXTURE_URL = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    HEADERS = {
        "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    }


class TelegramAPI:
    BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


class WeatherAPI:
    API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    ID_TO_EMOJI = {
        200: "🌩",
        201: "⛈️",
        202: "⛈",
        210: "🌩",
        211: "🌩",
        212: "🌩",
        221: "🌩",
        230: "🌩",
        231: "🌩",
        232: "⛈",
        300: "🌧",
        301: "🌧",
        302: "🌧",
        310: "🌧",
        311: "🌧",
        312: "🌧",
        313: "🌧",
        314: "🌧",
        321: "🌧",
        500: "🌧",
        501: "🌧",
        502: "🌧",
        503: "🌧",
        504: "🌧",
        511: "🌧",
        520: "🌧",
        521: "🌧",
        522: "🌧",
        531: "🌧",
        600: "🌨",
        601: "🌨",
        602: "🌨",
        611: "🌨",
        612: "🌨",
        613: "🌨",
        615: "🌨",
        616: "🌨",
        620: "🌨",
        621: "🌨",
        622: "🌨",
        701: "🌁",
        711: "🌁",
        721: "🌁",
        731: "🌁",
        741: "🌁",
        751: "🌁",
        761: "🌁",
        762: "🌁",
        771: "🌁",
        781: "🌁",
        800: "☀️",
        801: "🌤",
        802: "⛅",
        803: "🌥",
        804: "☁️",
    }


TEAMS = {
    "France": {"name": "France 🇫🇷", "person": "Fionnuala"},
    "England": {"name": "England 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "person": "Hannah"},
    "Belgium": {"name": "Belgium 🇧🇪", "person": "Jack"},
    "Spain": {"name": "Spain 🇪🇸", "person": "Lucy"},
    "Germany": {"name": "Germany 🇩🇪", "person": "Alex"},
    "Portugal": {"name": "Portugal 🇵🇹", "person": "Emma"},
    "Netherlands": {"name": "Netherlands 🇳🇱", "person": "Delia"},
    "Denmark": {"name": "Denmark 🇩🇰", "person": "Zoe"},
    "Croatia": {"name": "Croatia 🇭🇷", "person": "Paddy"},
    "Turkey": {"name": "Turkey 🇹🇷", "person": "Giulia"},
    "Italy": {"name": "Italy 🇮🇹", "person": "Grace"},
    "Poland": {"name": "Poland 🇵🇱", "person": "Nathalie"},
    "FYR Macedonia": {"name": "North Macedonia 🇲🇰", "person": "Giulia"},
    "Wales": {"name": "Wales 🏴󠁧󠁢󠁷󠁬󠁳󠁿", "person": "Zoe"},
    "Hungary": {"name": "Hungary 🇭🇺", "person": "Alex"},
    "Slovakia": {"name": "Slovakia 🇸🇰", "person": "Grace"},
    "Scotland": {"name": "Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿", "person": "Paddy"},
    "Finland": {"name": "Finland 🇫🇮", "person": "Delia"},
    "Czech Republic": {"name": "Czech Republic 🇨🇿", "person": "Nathalie"},
    "Russia": {"name": "Russia 🇷🇺", "person": "Fionnuala"},
    "Austria": {"name": "Austria 🇦🇹", "person": "Hannah"},
    "Ukraine": {"name": "Ukraine 🇺🇦", "person": "Lucy"},
    "Switzerland": {"name": "Switzerland 🇨🇭", "person": "Emma"},
    "Sweden": {"name": "Sweden 🇸🇪", "person": "Jack"},
}


SELECTIONS2 = {
    "Zoe": [
        "Denmark",
        "Wales",
    ],
    "Emma": [
        "Portugal",
        "Switzerland",
    ],
    "Alex": [
        "Germany",
        "Hungary",
    ],
    "Paddy": [
        "Croatia",
        "Scotland󠁳󠁣󠁴󠁿",
    ],
    "Fionnuala": [
        "France",
        "Russia"
    ],
    "Giulia": [
        "Turkey",
        "FYR Macedonia",
    ],
    "Delia": [
        "Netherlands",
        "Finland",
    ],
    "Hannah": [
        "England",
        "Austria",
    ],
    "Nathalie": [
        "Poland",
        "Czech Republic",
    ],
    "Grace": [
        "Italy",
        "Slovakia",
    ],
    "Lucy": [
        "Spain",
        "Ukraine",
    ],
    "Jack": [
        "Belgium",
        "Sweden",
    ],
}

SELECTIONS = {
    "Zoe": [
        "Denmark 🇩🇰",
        "Wales 🏴󠁧󠁢󠁷󠁬󠁳󠁿",
    ],
    "Emma": [
        "Portugal 🇵🇹",
        "Switzerland 🇨🇭",
    ],
    "Alex": [
        "Germany 🇩🇪",
        "Hungary 🇭🇺",
    ],
    "Paddy": [
        "Croatia 🇭🇷",
        "Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿",
    ],
    "Fionnuala": [
        "France 🇫🇷",
        "Russia 🇷🇺"
    ],
    "Giulia": [
        "Turkey 🇹🇷",
        "North Macedonia 🇲🇰",
    ],
    "Delia": [
        "Netherlands 🇳🇱",
        "Finland 🇫🇮",
    ],
    "Hannah": [
        "England 🏴󠁧󠁢󠁥󠁮󠁧󠁿",
        "Austria 🇦🇹",
    ],
    "Nathalie": [
        "Poland 🇵🇱",
        "Czech Republic 🇨🇿",
    ],
    "Grace": [
        "Italy 🇮🇹",
        "Slovakia 🇸🇰",
    ],
    "Lucy": [
        "Spain 🇪🇸",
        "Ukraine 🇺🇦",
    ],
    "Jack": [
        "Belgium 🇧🇪",
        "Sweden 🇸🇪",
    ],
}

LAST_16 = [
    "Netherlands",
    "Belgium",
    "Italy",
    "Wales",
    "Austria",
    "Denmark",
    "Switzerland",
    "France",
    "Czech Republic",
    "Sweden",
    "England",
    "Croatia",
    "Ukraine",
    "Spain",
    "Portugal",
    "Germany",
]
