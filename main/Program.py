import json
from Languages import Languages
from UserStatus import UserStatus
from GetHistoryUsers import GetHistory
from GetHistorySpecUser import GetHistorySpec
from Prediction import GetPrediction
from check_dataSet import check
from UserPredict import GetPredictionUser
from removeUser import removeUser
from avg import average
import requests
from totalTime import totalTime
import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path



base_url = "https://sef.podkolzin.consulting/api/users/lastSeen"

def get_users(offset):
    params = {"offset": offset}
    response = requests.get(base_url, params=params)
    content = response.text
    users_response = json.loads(content)

    return users_response

def main():
    print('1 - update CSV, 2 - default, 3 - get historical data, 4 - get historical user data, 5 - prediction, 6 - prediction for user,7 - remove users data, 8 - total time online for user, 9 - avg time online daily and weekly for user\n')
    command = input('\n')

    if command == "1":
        total = 200
        forbidden_users = set()
        with open("list_of_deleted.csv", "r") as f:
            forbidden_users.update(line.strip() for line in f)
        output_file = Path("main/outuput.csv")
        
        with output_file.open(mode="w", encoding="utf-8") as sw:
            sw.write("id,Day,Date,LastSeen,isOnline\n")

            for i in range(0, total, 20):
                users_response = get_users(i)
                total = users_response["total"]
                now = datetime.now().strftime("%A,%d-%m-%Y %H:%M:%S")
                
                for user in users_response["data"]:
                    if user['userId'] in forbidden_users:
                        continue
                    if user['isOnline']:
                        sw.write(f"{user['userId']},{now},Nan,{user['isOnline']}\n")
                    else:
                        lastSeen = datetime.fromisoformat(user['lastSeenDate'])
                        lastSeen_norm = lastSeen.strftime("%d-%m-%Y %H:%M:%S")
                        sw.write(f"{user['userId']},{now},{lastSeen_norm},{user['isOnline']}\n")
                        
    elif command == "2":
        total = 200
        phrases = []

        print("Яку мову хочете обрати/What language you want to choose: 1 - Українська/Ukranian, 2 - English/Англійська")
        input_lang = input()
        while input_lang not in ("1", "2"):
            print("Невірний ввід/Invalid input. Введіть 1 або 2/Enter 1 or 2.")
            input_lang = input()

        phrases = Languages.Ukrainian if input_lang == "1" else Languages.English

        for i in range(0, total, 20):
            users_response = get_users(i)
            total = users_response["total"]
            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            for user in users_response["data"]:
                if user["isOnline"]:
                    print(f"{user['nickname']} {phrases[0]}")
                else:
                    status = UserStatus.get_status(user["lastSeenDate"], phrases)
                    print(f"{user['nickname']} {phrases[1]} {status}")

    elif command == "3":
        dataSet_path = "main/outuput.csv"
        path = check(dataSet_path)
        searchDate = input("Enter date in format dd-mm-yy hh-mm-ss: ")
        print(GetHistory(path, searchDate))

    elif command == "4":
        dataSet_path = "main/outuput.csv"
        path = check(dataSet_path)
        searchId = input("Enter user's id: ")
        searchDate = input("Enter date in format dd-mm-yy hh:mm:ss: ")
        print(GetHistorySpec(path, searchId, searchDate))

    elif command == "5":
        dataSet_path = "main/outuput.csv"
        path = check(dataSet_path)
        input_date = input("Enter a date in dd-mm-yy hh:mm:ss format: ")
        print(GetPrediction(path, input_date))
    elif command == "6":
        dataSet_path = "main/outuput.csv"
        path = check(dataSet_path)
        tolerance = input("Input acceptable tolerance for prediction : ")
        searchId = input("Enter user's id: ")
        searchDate = input("Enter date in format dd-mm-yy hh:mm:ss: ")
        print(GetPredictionUser(path, searchId, searchDate, tolerance))
    elif command == "7":
        dataSet_path = "main/outuput.csv"
        path = check(dataSet_path)
        searchId = input("Enter user's id: \n")
        print(removeUser(dataSet_path, searchId))
    elif command == "8":
        dataSet_path = "main/testTotatTime.csv"
        path = check(dataSet_path)
        searchId = input("Enter user's id: \n")
        print(totalTime(dataSet_path, searchId))
    elif command == "9":
        dataSet_path = "main/testAvg.csv"
        path = check(dataSet_path)
        searchId = input("Enter user's id: \n")
        print(average(dataSet_path, searchId))
        

if __name__ == "__main__":
    main()
