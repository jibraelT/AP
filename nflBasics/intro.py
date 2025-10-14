import nfl_data_py as nfl
import pandas as pd
import os


path = os.path.abspath("nflData/nfl_records_2024.csv")

records = pd.read_csv(path)


#print(records.head())
#print(records.columns)

teams = nfl.import_team_desc()
team_stats =nfl.import_seasonal_data
#print(teams)

win_totals= nfl.import_win_totals()
print(win_totals)
    