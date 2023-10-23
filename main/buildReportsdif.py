import pandas as p
from main.avgReports import average
from main.totalTimeReports import totalTime
from main.MaxTimeMinTime import maximumTime
from main.MaxTimeMinTime import minimumTime
from pathlib import Path

def build(path, choices):
    df = p.read_csv(path)
    unique_ids = df['id'].unique()

    choice = choices.split(' ')
    output_file = Path("main/reportDataBase.csv")
    with output_file.open(mode="w", encoding="utf-8") as sw:
        sw.write("id,dailyAvg,weeklyAvg,total,min,max\n")
        for id in unique_ids:
            dailyAvg, weeklyAvg = average(path, id)
            if choice[0] == '0':
                dailyAvg = 'Nan'
            if choice[1] == '0':
                weeklyAvg = 'Nan'
            total = totalTime(path, id) 
            if choice[2] == '0':
                total = 'Nan'
            max = maximumTime(path, id)
            if choice[3] == '0':
                max = 'Nan'
            min = minimumTime(path, id)
            if choice[4] == '0':
                min = 'Nan'
            sw.write(f"{id},{dailyAvg},{weeklyAvg},{total},{max},{min}\n")
    return "Created report base"
