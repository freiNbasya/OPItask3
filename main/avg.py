import pandas as p

def average(path, inputId):
    df = p.read_csv(path)
    id_intervals = df[df['id'] == inputId]
    daily_total_time = {}
    weekly_total_time = {}

    for index, value in id_intervals.iterrows():
        if value['LastSeen'] == "Nan":
            start = p.to_datetime(value['Date'])
        elif value['LastSeen'] != "Nan":
            end = p.to_datetime(value['LastSeen'])
            if start.date() not in daily_total_time:
                daily_total_time[start.date()] = p.Timedelta(0)
            if start.strftime('%U-%Y') not in weekly_total_time:
                weekly_total_time[start.strftime('%U-%Y')] = p.Timedelta(0)
            daily_total_time[start.date()] += end - start
            weekly_total_time[start.strftime('%U-%Y')] += end - start
            start = end

    daily_average = sum(daily_total_time.values(), p.Timedelta(0)) / len(daily_total_time)
    weekly_average = sum(weekly_total_time.values(), p.Timedelta(0)) / len(weekly_total_time)

    return f"Average daily time for this user is {daily_average}, Average weekly time for this user is {weekly_average}"

