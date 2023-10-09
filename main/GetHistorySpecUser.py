import pandas as p 

def GetHistorySpec(dataSet_path):
    dataSet = p.read_csv(dataSet_path)
    searchId = input("Enter user's id: ")
    searchDate = input("Enter date in format dd-mm-yy hh-mm-ss: ")
    dataSetReq = (dataSet[(dataSet["isOnline"]==True) & (dataSet["id"]==searchId) & (dataSet["Date"]==searchDate) ]).shape[0]
    if dataSetReq == 1:
        print("User is online")
    else:
        dataSetLast = dataSet[(dataSet["id"]==searchId)]
        print(f"User is offline last time seen online: {dataSetLast['LastSeen'].values}")