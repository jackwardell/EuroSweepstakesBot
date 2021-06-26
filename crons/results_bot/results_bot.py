from datetime import date, timedelta

import requests
import random
from shared.static import FootballAPI, LAST_16
from shared.static import TEAMS
from shared.utils import ping_telegram, people_knocked_out_today, knock_out, teams_knocked_out_today
from shared.utils import ping_telegram_with_image
from shared.utils import write_to_spiderman_image

BEAT_WORDING = {
    0: "drew with",
    1: "beat",
    2: "rekt",
    3: "totally destroyed",
    4: "fucked",
    5: "annihilated",
}


rude_words = [
    "SHITHEAD",
    "TWAT",
    "FUCKING LOSER",
    "MOTHERFUCKING CUNT",
    "BASTARD",
    "WASTEMAN",
    "MEGA TWAT",
    "SILLY SAUSAGE",
    "STEAMING PILE OF SHIT",
    "SMELLY POO POO",
    "DIRTY DOG",
    "FOUL PERSON"
]

RESULT_MESSAGE = "🏆 {winning_team} {action} {losing_team} {score} {period}😞\n{comment}"


def main():
    messages = []

    params = {
        "league": FootballAPI.LEAGUE_ID,
        "season": FootballAPI.SEASON,
        "from": str(date.today() - timedelta(days=1)),
        "to": str(date.today() - timedelta(days=1)),
    }
    response = requests.get(
        FootballAPI.FIXTURE_URL, headers=FootballAPI.HEADERS, params=params
    )

    for fixture in response.json()["response"]:
        home_team = fixture["teams"]["home"]["name"]
        away_team = fixture["teams"]["away"]["name"]
        home_win = fixture["teams"]["home"]["winner"]
        away_win = fixture["teams"]["away"]["winner"]
        winning_team = (
            home_team
            if (home_win is True and away_win is False)
            else away_team
            if (home_win is False and away_win is True)
            else home_team
        )
        losing_team = (
            home_team
            if (home_win is False and away_win is True)
            else away_team
            if (home_win is True and away_win is False)
            else away_team
        )
        home_score = fixture["goals"]["home"]
        away_score = fixture["goals"]["away"]
        winning_team_score = (
            home_score
            if (home_win is True and away_win is False)
            else away_score
            if (home_win is False and away_win is True)
            else home_score
        )
        losing_team_score = (
            home_score
            if (home_win is False and away_win is True)
            else away_score
            if (home_win is True and away_win is False)
            else away_score
        )
        score = f"{winning_team_score}-{losing_team_score}"
        score_difference = abs(home_score - away_score)
        # is_draw = score_difference == 0
        winner = TEAMS[winning_team]["person"]
        loser = TEAMS[losing_team]["person"]

        # import IPython; IPython.embed()

        home_extratime = fixture["score"]["extratime"]["home"]
        away_extratime = fixture["score"]["extratime"]["away"]
        is_extratime = home_extratime or away_extratime

        home_penalties = fixture["score"]["penalty"]["home"]
        away_penalties = fixture["score"]["penalty"]["away"]
        is_penalties = home_penalties or away_penalties

        if is_penalties:
            period = "in penalties 🦵⚽ "
        elif is_extratime:
            period = "in extratime ➕⏱️ "
        else:
            period = ""

        comment = f"🎉 Well done {winner} and get rekt {loser} 💀"
        # if not is_draw else "🥱 It was a draw... lame 💤"

        try:
            action = BEAT_WORDING[score_difference]
        except:
            action = "beat so badly I didn't even program how badly the beating was"

        values = {
            "winning_team": TEAMS[winning_team]["name"],
            "losing_team": TEAMS[losing_team]["name"],
            "action": action,
            "score": score,
            "period": period,
            "comment": comment,
        }
        data = {"values": values, "winner": winner, "loser": loser}
        messages.append(data)

    comment = "⚔️ Here are the results from today 👇"

    if messages:
        ping_telegram(comment)

        for data in messages:
            message = ping_telegram(RESULT_MESSAGE.format(**data["values"]))
            data['message_id'] = message.message_id

    # for data in messages:
    #     if data["winner"] == data["loser"]:
    #         file_path = write_to_spiderman_image(data["winner"])
    #         ping_telegram_with_image("lol 🤔", file_path, data['message_id'])

    # knocked out team
    for data in messages:
        msgs = []
        person = data["loser"]
        team = data["values"]["losing_team"]
        if person != "Jack":
            msg = f"❌ {team} is out! Get rekt {person} ☠️"
        else:
            msg = f"😔 Sorry {person}, {team} is out! Have a commiseration beer on me 🍺"
        msgs.append(msg)
        knock_out(team)
        ping_telegram("\n".join(msgs))

    # knocked out person
    ppl = people_knocked_out_today()
    msgs = []
    for p in ppl:
        if p != "Jack":
            msgs.append(f"❌ GET FUCKING REKT {p.upper()}, YOU'RE OUT 💀\nYOU ARE A {random.choice(rude_words)}!")
        else:
            msgs.append(f"Tough break Jack... looks like you're out, don't worry you can take Giulia's money for being last 😉")
    ping_telegram("\n".join(msgs))


if __name__ == "__main__":
    main()
