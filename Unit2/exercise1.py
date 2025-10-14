import pandas as pd
import nfl_data_py as nfl

from helperFunction import get_team_records

schedules = nfl.import_schedules([2024])

#print(schedules.columns.tolist())

records = get_team_records(2020)

print(records[['wins']].mean())
















