from datetime import date
from datetime import datetime
from datetime import timedelta
from shared.utils import get_peckham_weather_emoji
import requests

from shared.static import TEAMS, FootballAPI
from shared.utils import ping_telegram

FIXTURE_MESSAGE = "🤝 Teams: {home_team} play {away_team} \n🏟️ Stadium: {stadium} in {city} 🧑‍🤝‍🧑\n🦵 Kick Off: {kick_off} today ⏱️\n🔢 Round: {round} 💫\n⚔️ Rivals: {home_rival} vs. {away_rival} 😈"


def main():
    messages = []

    params = {
        "league": FootballAPI.LEAGUE_ID,
        "season": FootballAPI.SEASON,
        "from": str(date.today()),
        "to": str(date.today()),
    }
    response = requests.get(
        FootballAPI.FIXTURE_URL, headers=FootballAPI.HEADERS, params=params
    )

    for fixture in response.json()["response"]:
        data = {
            "home_team": TEAMS[fixture["teams"]["home"]["name"]]["name"],
            "away_team": TEAMS[fixture["teams"]["away"]["name"]]["name"],
            "stadium": fixture["fixture"]["venue"]["name"],
            "city": fixture["fixture"]["venue"]["city"],
            "country": fixture["teams"]["home"]["name"],
            "kick_off": str(
                (
                        datetime.fromisoformat(fixture["fixture"]["date"])
                        + timedelta(hours=1)
                ).time()
            ),
            "round": fixture["league"]["round"],
            "home_rival": TEAMS[fixture["teams"]["home"]["name"]]["person"],
            "away_rival": TEAMS[fixture["teams"]["away"]["name"]]["person"],
        }
        messages.append(FIXTURE_MESSAGE.format(**data))

    if messages:
        try:
            weather = get_peckham_weather_emoji()
        except:
            weather = "🌞"

        ping_telegram(
            f"{weather} Good Morning Friends {weather}\n⚽ Today there {len(messages)} matches. Here are the fixtures 👇")

        for message in messages:
            ping_telegram(message)

        ping_telegram("🍀 Good luck everyone! 🍀")


if __name__ == "__main__":
    main()
