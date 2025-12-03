from helperLogic import plot_position_stat_bar
import matplotlib.pyplot as plt
import pandas as pd

stats = plot_position_stat_bar(2022,"RB", 'rushing_yards',save_path="rb_rushing_2022.png", top_n=20)  
stats = plot_position_stat_bar(2023,"RB",'rushing_yards',save_path="rb_rushing_2023.png", top_n=20)  
stats = plot_position_stat_bar(2024,"RB",'rushing_yards',save_path="rb_rushing_2024.png", top_n=20)  
print(stats)

print("Derrick henry was the rushing leader for ove rthis period of time because even tho he never reached number one he still stayed at a steady rate")




percentage = plot_position_stat_bar(2022,"QB", 'passing_yards',save_path="qb_passing_2022.png", top_n=20)  
percentage = plot_position_stat_bar(2023,"QB",'passing_yards',save_path="qb_passing_2023.png", top_n=20)  
percentage = plot_position_stat_bar(2024,"QB",'passing_yards',save_path="qb_passing_2024.png", top_n=20)
print(percentage)

print(" I would say it was patrick mahomes because of his steady rate. But he has began to decline ovee the period of this time")



















