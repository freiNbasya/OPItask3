import pandas as p
def GetHistory(dataSet_path):
    dataSet = p.read_csv(dataSet_path)
    date = input("Enter date in format dd-mm-yy hh-mm-ss: ")
    dataSetReq = (dataSet[(dataSet["isOnline"]==True) & (dataSet["Date"]==date) ]).shape[0]
    print(dataSetReq)