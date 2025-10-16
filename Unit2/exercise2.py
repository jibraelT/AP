import pandas as pd
import nfl_data_py as nfl
from helperFunction import get_season_Results_By_team
from helperFunction import get_team_records

schedules = get_team_records(2025)
print(schedules)

top6_Teams = ['TB', 'IND','LA','BUF','SF','SEA','PIT']

team_1=get_season_Results_By_team(2025,'TB')
team_2=get_season_Results_By_team(2025,'INN')
team_3=get_season_Results_By_team(2025,'LA')
team_4=get_season_Results_By_team(2025,'BUF')
team_5=get_season_Results_By_team(2025,'SF')
team_6=get_season_Results_By_team(2025,'SEA')

print(team_1)
print(team_2)
print(team_3)
print(team_4)
print(team_5)
print(team_6)

print('the IND'
' and has  the best point diffrence this season')
print('the seahawks have the worst point diffrence this season')
print(' the best home point diffrence is a tie between TB and BUF')
print(' the best away point diffrence is PIT ')


def pdCheck():
    print("please enter a number")
    number = input
    values= []
    calculate ='y'
    while number != 'stop':
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('doing calculation ')
pdCheck





