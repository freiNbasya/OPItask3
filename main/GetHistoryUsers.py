import pandas as p
def GetHistory(dataSet_path, enterDate):
    dataSet = p.read_csv(dataSet_path)
    date = enterDate
    dataSetReq = (dataSet[(dataSet["isOnline"]==True) & (dataSet["Date"]==date) ]).shape[0]
    return dataSetReq