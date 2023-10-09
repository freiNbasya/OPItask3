import pandas as p
def check():
    try:
        dataSet_path = "C:/Labs_Kse/OPI/task3OPI/main/outuput.csv"
        dataSet = p.read_csv(dataSet_path)
        print("DataSet loaded")
        return dataSet_path
    except FileNotFoundError:
        print("DataSet not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")