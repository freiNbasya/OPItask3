import pandas as p

def removeUser(path, inputId):
    df = p.read_csv(path)
    deleted_rows = df[df['id'] == inputId]
    deleted_rows = deleted_rows['id']
    df = df[df['id'] != inputId]
    df.to_csv(path, index=False)
    deleted_file_path = './main/list_of_deleted.csv'
    deleted_rows.to_csv(deleted_file_path,mode='a', index=False, header=False)
    return "User deleted"