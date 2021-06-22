from datetime import date
from datetime import timedelta

import requests

from shared.static import FootballAPI
from shared.static import TEAMS
from shared.utils import ping_telegram

BEAT_WORDING = {
    0: "drew with",
    1: "beat",
    2: "rekt",
    3: "totally destroyed",
    4: "fucked",
    5: "annihilated",
    6: "eviscerated"
}

RESULT_MESSAGE = "🏆 {winning_team} {action} {losing_team} {score} 😞\n{comment}"


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
        home_team = fixture['teams']['home']['name']
        away_team = fixture['teams']['away']['name']
        home_win = fixture['teams']['home']['winner']
        away_win = fixture['teams']['away']['winner']
        winning_team = home_team if (home_win is True and away_win is False) else away_team if (
                home_win is False and away_win is True) else home_team
        losing_team = home_team if (home_win is False and away_win is True) else away_team if (
                home_win is True and away_win is False) else away_team
        home_score = fixture['goals']['home']
        away_score = fixture['goals']['away']
        winning_team_score = home_score if (home_win is True and away_win is False) else away_score if (
                home_win is False and away_win is True) else home_score
        losing_team_score = home_score if (home_win is False and away_win is True) else away_score if (
                home_win is True and away_win is False) else away_score
        score = f"{winning_team_score}-{losing_team_score}"
        score_difference = abs(home_score - away_score)
        is_draw = score_difference == 0
        winner = TEAMS[winning_team]['person']
        loser = TEAMS[losing_team]['person']
        comment = f"🎉 Well done {winner} and get rekt {loser} 💀" if not is_draw else "🥱 It was a draw... lame 💤"

        try:
            action = BEAT_WORDING[score_difference]
        except:
            action = "beat so badly I didn't even program how badly the beating was"

        data = {
            "winning_team": TEAMS[winning_team]["name"],
            "losing_team": TEAMS[losing_team]["name"],
            "action": action,
            "score": score,
            "comment": comment

        }
        messages.append(RESULT_MESSAGE.format(**data))

    comment = "⚔️ Here are the results from today 👇"

    if messages:
        ping_telegram(comment)

        for message in messages:
            ping_telegram(message)


if __name__ == "__main__":
    main()

