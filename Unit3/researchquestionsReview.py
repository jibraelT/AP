from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, nfl
import matplotlib.pyplot as plt

# Columns available to research based on year and position
# columnData = get_position_columns(2024, "QB")

'1. How much does QB pass accuracy influence team wins ? '
teamRecord = get_team_records(2024)
#print(teamRecord)

advanceStats =  get_advanced_team_records(2024)
print(advanceStats)

qbData = weeklyPlayerStats(2024, 'QB')
#print(qbData)


def get_team_records(year):
    games = nfl.import_schedules([year])

    if "season_type" in games.columns:
        games = games[games["season_type"] == "REG"]
    else:
        games = games[games["game_type"] == "REG"]

    games = games.dropna(subset=["home_score", "away_score"])

    home = games[["home_team", "home_score", "away_score"]].rename(
        columns={"home_team": "team", "home_score": "points_for", "away_score": "points_against"}
    )
    home["win"] = (home["points_for"] > home["points_against"]).astype(int)

    away = games[["away_team", "away_score", "home_score"]].rename(
        columns={"away_team": "team", "away_score": "points_for", "home_score": "points_against"}
    )
    away["win"] = (away["points_for"] > away["points_against"]).astype(int)





'2. Does defensive turnovers contribute to a teams win percentage ? '
print(" I believe that this question is a relation because it is trying to see if there is a relationship between turnovers and win percentages. " \
"The defensive turnovers does not contribute to team wins")

'3. Who has the most passing yards of all time ? '
print(" You can't really awnser this question because its to vague, with the data that i have it stops at 1999.")


