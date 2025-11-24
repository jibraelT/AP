from helperLogic import get_player_stats_by_name, get_advanced_team_records, plot_weekly_player_stats,plot_player_stat, get_season_Results_By_team,weeklyPlayerStats, get_team_records
import matplotlib.pyplot as nfl







#1. Which division had thje strongest defense based on yards allowed per game in 2024


   

teamData = get_advanced_team_records(2024)

teamRes = get_season_Results_By_team(2024,"PHI")

print(get_team_records)


#2. Which WR had the most targets vs their receptions(catches) in 2024.
stats = weeklyPlayerStats(2024, "WR")  
print(stats)
plot_player_stat(stats, stat="receiving_tds", top_n=10, title="WR receiving tds (2024)", save_path="WR_receiving_tds_2024.png"  )




#3. Does time of possesion strongly correlate with wins in 2024.

print(' I am 100% positive that this question is a comparitive because it is using a key word correalte which means go with or into. But I can not write a code for this due to lack of data.')






