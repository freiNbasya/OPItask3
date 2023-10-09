import pandas as p
from datetime import datetime, timedelta

def GetPredictionUser(path):
    df = p.read_csv(path)

    # Input date from the user
    tolerance = input("Input acceptable tolerance: ")
    input_id = input("Enter id: ")
    input_date = input("Enter date: ")
    # Parse the input date to a datetime object
    input_date = p.to_datetime(input_date, format="%d-%m-%Y %H:%M:%S")

    # Extract the day of the week from the input date
    input_day = input_date.strftime("%A")

    # Filter the DataFrame based on the input day
    filtered_df = df[(df["Date"].str[11:19] == input_date.strftime("%H:%M:%S")) & (df["isOnline"]== True) & (df["id"]==input_id) & (df["Day"] == input_day)]
    filtered_shape = filtered_df.shape[0]
    total_weeks = df[(df["id"]==input_id) & (df["Day"] == input_day)]
    total_shape = total_weeks.shape[0]
    # Print the filtered DataFrame
    if not filtered_df.empty:
        if filtered_shape/total_shape > float(tolerance):
            print("User will be online")
        else:
            print("user will be offline")
    else:
        print("No entries")