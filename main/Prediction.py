import pandas as p
from datetime import datetime, timedelta

def GetPrediction(path):
    df = p.read_csv(path)

    input_date = input("Enter a date in dd-mm-yy hh-mm format: ")

    input_date = p.to_datetime(input_date, format="%d-%m-%Y %H:%M:%S")

    input_day = input_date.strftime("%A")

    filtered_df = df[(df["Date"].str[11:19] == input_date.strftime("%H:%M:%S")) & (df["isOnline"]== True) & (df["Day"] == input_day)]
    filtered_shape = filtered_df.shape[0]
    date_groups =filtered_df.groupby("Date")
    number_of_groups = date_groups.ngroups
    

    if not filtered_df.empty:
        print(f"Prediction {filtered_shape//number_of_groups}")
    else:
        print("No entries")