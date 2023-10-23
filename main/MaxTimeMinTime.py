import pandas as p

def maximumTime(path, inputId):
    df = p.read_csv(path)
    id_intervals = df[df['id']==inputId]
    start = None
    end = None
    total_duration = []
    for index,value in id_intervals.iterrows():
        if value['LastSeen'] == "Nan":
            start = value['Date']
        elif value['LastSeen'] != "Nan":
            end = value['LastSeen']
            end = p.to_datetime(end)
            start = p.to_datetime(start)
            total_duration.append((end - start).total_seconds())
            start = None
    return max(total_duration)

def minimumTime(path, inputId):
    df = p.read_csv(path)
    id_intervals = df[df['id']==inputId]
    start = None
    end = None
    total_duration = []
    for index,value in id_intervals.iterrows():
        if value['LastSeen'] == "Nan":
            start = value['Date']
        elif value['LastSeen'] != "Nan":
            end = value['LastSeen']
            end = p.to_datetime(end)
            start = p.to_datetime(start)
            total_duration.append((end - start).total_seconds())
            start = None
    return min(total_duration)