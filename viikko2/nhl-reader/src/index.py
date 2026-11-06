"""Main entry point for the application"""

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

def create_table(season, nationality, players):
    """creates a table with player information"""

    table = Table(title=f"Top scorers of {nationality} season {season}")

    table.add_column("Name", style="medium_orchid", no_wrap=True)
    table.add_column("Team", style="deep_pink4")
    table.add_column("Goals", justify="right", style="sky_blue1")
    table.add_column("Assists", justify="right", style="orchid1")
    table.add_column("Points", justify="right", style="gold1")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    return table


def main():
    """Asks user for season and nationality, then fetches information"""

    console = Console()
    season= Prompt.ask("Select season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    nationality = Prompt.ask(
        "Select nationality",
        choices=stats.nationalities(),
        default="FIN"
    )

    players = stats.top_scorers_by_nationality(nationality)
    console.print(create_table(season, nationality, players))

main()
