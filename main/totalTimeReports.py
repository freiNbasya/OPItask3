import pandas as p

def totalTime(path, inputId):
    df = p.read_csv(path)
    id_intervals = df[df['id']==inputId]
    start = None
    total_time = p.Timedelta(0)
    end = None
    for index,value in id_intervals.iterrows():
        if value['LastSeen'] == "Nan":
            start = value['Date']
        elif value['LastSeen'] != "Nan":
            end = value['LastSeen']
            end = p.to_datetime(end)
            start = p.to_datetime(start)
            total_time += (end - start)
    total_time = total_time.total_seconds()
    return total_time
