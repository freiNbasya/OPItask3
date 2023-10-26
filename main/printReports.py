import pandas as pd

def printReports(dataset_path):
    df = pd.read_csv(dataset_path)
    for index, row in df.iterrows():
        output = []
        if row['id'] != 'Nan':
            output.append(f'userId: {row["id"]}')
        if row['dailyAvg'] != 'Nan':
            output.append(f'dailyAvg: {row["dailyAvg"]}')
        if row['weeklyAvg'] != 'Nan':
            output.append(f'weeklyAvg: {row["weeklyAvg"]}')
        if row['total'] != 'Nan':
            output.append(f'total: {row["total"]}')
        if row['min'] != 'Nan':
            output.append(f'min: {row["min"]}')
        if row['max'] != 'Nan':
            output.append(f'max: {row["max"]}')
        print('\n'.join(output))
    return 'printed reports'
