import pandas as p
from datetime import datetime, timedelta

def GetPredictionUser(path, enterId, enterDate, tol_value):
    df = p.read_csv(path)

    
    tolerance = tol_value
    input_id = enterId
    input_date = enterDate
    
    input_date = p.to_datetime(input_date, format="%d-%m-%Y %H:%M:%S")

    
    input_day = input_date.strftime("%A")

    
    filtered_df = df[(df["Date"].str[11:19] == input_date.strftime("%H:%M:%S")) & (df["isOnline"]== True) & (df["id"]==input_id) & (df["Day"] == input_day)]
    filtered_shape = filtered_df.shape[0]
    total_weeks = df[(df["id"]==input_id) & (df["Day"] == input_day)]
    total_shape = total_weeks.shape[0]
    
    if not filtered_df.empty:
        if filtered_shape/total_shape > float(tolerance):
            return "User will be online"
        else:
            return "user will be offline"
    else:
        print("No entries")