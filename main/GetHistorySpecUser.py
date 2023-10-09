import pandas as p 

def GetHistorySpec(dataSet_path, enterId, enterDate):
    dataSet = p.read_csv(dataSet_path)
    searchId = enterId
    searchDate = enterDate
    dataSetReq = (dataSet[(dataSet["isOnline"]==True) & (dataSet["id"]==searchId) & (dataSet["Date"]==searchDate) ]).shape[0]
    if dataSetReq == 1:
        return "User is online"
    else:
        dataSetLast = dataSet[(dataSet["id"]==searchId)]
        return f"User is offline last time seen online: {dataSetLast['LastSeen'].values}"