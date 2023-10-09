import pandas as p
def check(inputPath):
    try:
        dataSet_path = inputPath
        dataSet = p.read_csv(dataSet_path)
        print("DataSet loaded")
        return dataSet_path
    except FileNotFoundError:
        print("DataSet not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")