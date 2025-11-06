from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "WR")  
print(stats)
plot_player_stat(stats, stat="receiving_tds", top_n=10, title="WR receiving tds (2024)", save_path="WR_receiving_tds_2024.png"  )


#yoou can copy and paste this code from the ap repo. the document is called exercise.
#try to run the code above

# if you have aan error while multiplying raise your hand I will help you.


# 2) One-liner wrapper:

#plot_weekly_player_stats(2024, "RB", stat="rushing_yards", top_n=15, week=[1,2,3], save_path="rb_rushing_yards_wk1-17.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.

# 1. Use each helper function to find your own metric to visualize. use the weeklyPlayerStats function to find positions and stat columns by name
 
# 2. Find the player with the most touchdowns in 2024?
print("lamar jackson has the most touchdowns in 2024")

# 3. find the player with the highest total passing yards in 2024
print('jared golf has the highest passing yards')

# 4. which player had the highest rushing yards in week 1 and in week 17?
print("derrick hengry had the highest rushing in week 1 but saquon barkley had the highest in week 17.")