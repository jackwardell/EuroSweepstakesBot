from shared.static import LAST_16
from shared.static import SELECTIONS
from shared.static import TEAMS
from shared.utils import ping_telegram


def teams_in():
    msg = "The group stages are over! ✔️\nHere are the teams that remain 👇\n{}"
    teams = [TEAMS[team]["name"] for team in LAST_16]

    return msg.format("\n".join(teams))


def people_in():
    msg = "Which means here is who's in and who's out 👇\n{}"
    msgs = []
    sub_msg = "✅ {person} ({team1}{team2})"

    last_16_emojis = [TEAMS[t]["name"] for t in LAST_16]

    for person, teams in SELECTIONS.items():
        match = list(set(teams) & set(last_16_emojis))

        if match:
            if len(match) == 2:
                team1 = match[0]
                team2 = f" & {match[1]}"

            else:
                team1 = match[0]
                team2 = ""

            msgs.append(sub_msg.format(person=person, team1=team1, team2=team2))

        else:
            msgs.append(f"❌ {person} you're out (get rekt loser) ☠️")

    return msg.format("\n".join(sorted(msgs)))


def main():
    ping_telegram(teams_in())
    ping_telegram(people_in())


if __name__ == "__main__":
    main()
