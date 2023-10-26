import pandas as pd

def printReportsAvg(dataset_path):
    df = pd.read_csv(dataset_path)
    totalDaily = 0
    totalWeekly = 0
    totalTotal = 0
    totalMin = 0
    totalMax = 0
    totalIds = 0
    for index, row in df.iterrows():
        if row['dailyAvg'] != 'Nan':
            secondsDaily = pd.to_timedelta(row['dailyAvg']).total_seconds()
            totalDaily += secondsDaily
        if row['weeklyAvg'] != 'Nan':
            secondsWeekly = pd.to_timedelta(row['weeklyAvg']).total_seconds()
            totalWeekly += secondsWeekly
        if row['total'] != 'Nan':
            totalTotal += int(row['total'])
        if row['min'] != 'Nan':
            totalMin += int(row['min'])
        if row['max'] != 'Nan':
            totalMax += int(row['max'])
        totalIds +=1
    totalDailyAvg = totalDaily // totalIds
    totalWeeklyAvg = totalWeekly // totalIds
    totalTotalAvg = totalTotal // totalIds
    totalMinAvg = totalMin // totalIds
    totalMaxAvg = totalMax // totalIds
    print(f"dailyAverage: {totalDailyAvg}, weeklyAverage: {totalWeeklyAvg}, totalAverage: {totalTotalAvg}, minAverage: {totalMinAvg}, maxAverage: {totalMaxAvg}")
    
    return 'printed reports'
