from helperLogic import plot_position_stat_bar, plot_player_stat_by_week, get_player_stats
import matplotlib.pyplot as plt
import pandas as pd

print(" some indicators that can tell somebody if a player is a washed could be a decease in rushing yards. Another one can be a decrease in average touchdowns throuth a year." \
"Then maybe rushing avg yards is one that can show someone is washed. I would also Like to count receiving becasue wrs, rb, Te, can all have receiving yards.")


position = plot_position_stat_bar(2022,"RB", 'rushing_yards',save_path="rb_rushing_2022.png", top_n=20)  
position = plot_position_stat_bar(2023,"RB",'rushing_yards',save_path="rb_rushing_2023.png", top_n=20)  #position = plot_position_stat_bar(2024,"RB",'rushing_yards',save_path="rb_rushing_2024.png", top_n=20)  
print(position)


tds = plot_position_stat_bar(2022,"RB", 'rushing_tds',save_path="rb_touchdowns_2022.png", top_n=20)  
tds = plot_position_stat_bar(2023,"RB",'rushing_tds',save_path="rb_touchdowns_2023.png", top_n=20)  
tds = plot_position_stat_bar(2024,"RB",'rushing_tds',save_path="rb_touchdowns_2024.png", top_n=20)  
print(tds)



Eelliot= get_player_stats(2024,'Ezekiel',' Elliott')
#print(Eelliot)


Eelliotstats=plot_player_stat_by_week(2016, 'Ezekiel','Elliott',"rushing_yards", save_path='Ezekial Elliot rushing_yards 2024')
print(Eelliotstats)

print('I beleive that Ezekiel Elliott, is now a washed player. I beleive this because his average yards per carry is dropping through the years of 2022 to 2024. showing a decrease in stats.' \
'')
