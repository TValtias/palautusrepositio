import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nationality = "FIN"
    print(f"Players from {nationality}: \n")

    finns = [p for p in players if p.nationality == nationality]
    finns.sort(key=lambda p: p.goals + p.assists, reverse = True)
    for player in finns:
            print(player)

main()