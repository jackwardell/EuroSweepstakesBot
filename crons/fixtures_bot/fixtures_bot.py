from datetime import date
from datetime import datetime
from datetime import timedelta

import requests

from shared.static import FootballAPI
from shared.static import TEAMS
from shared.utils import get_peckham_weather_emoji
from shared.utils import ping_telegram
from shared.utils import ping_telegram_with_image
from shared.utils import write_to_spiderman_image

FIXTURE_MESSAGE = "š¤ Teams: {home_team} play {away_team} \nšļø Stadium: {stadium} in {city} š§āš¤āš§\nš¦µ Kick Off: {kick_off} today ā±ļø\nš¢ Round: {round} š«\nāļø Rivals: {home_rival} vs. {away_rival} š"


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
        messages.append(data)

    weather = get_peckham_weather_emoji()

    comment = "Here are the fixtures š" if messages else "Just chill the fuck out š»"

    ping_telegram(
        f"{weather} Good Morning Friends {weather}\nā½ Today there {len(messages)} matches. {comment}")

    if messages:
        for data in messages:
            message = ping_telegram(FIXTURE_MESSAGE.format(**data))
            data['message_id'] = message.message_id

        ping_telegram("š Good luck everyone! š")

    for data in messages:
        if data["home_rival"] == data["away_rival"]:
            file_path = write_to_spiderman_image(data["home_rival"])
            ping_telegram_with_image("lol š¤", file_path, data['message_id'])


if __name__ == "__main__":
    main()
