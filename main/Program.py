import json
from Languages import Languages
from UserStatus import UserStatus
from GetHistoryUsers import GetHistory
from GetHistorySpecUser import GetHistorySpec
from Prediction import GetPrediction
from check_dataSet import check
from UserPredict import GetPredictionUser
import requests
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
    print("1 - update CSV, 2 - default, 3 - get historical data, 4 - get historical user data, 5 - prediction, 6 - prediction for user")
    command = input()

    if command == "1":
        total = 200
        output_file = Path("C:/Labs_Kse/OPI/task3OPI/main/outuput.csv")

        with output_file.open(mode="w", encoding="utf-8") as sw:
            sw.write("id,Day,Date,LastSeen,isOnline\n")

            for i in range(0, total, 20):
                users_response = get_users(i)
                total = users_response["total"]
                now = datetime.now().strftime("%A,%d-%m-%Y %H:%M:%S")
                
                for user in users_response["data"]:
                    if user['isOnline']:
                        sw.write(f"{user['userId']},{now},None,{user['isOnline']}\n")
                    else:
                        lastSeen = datetime.fromisoformat(user['lastSeenDate'])
                        lastSeen_norm = lastSeen.strftime("%d-%m-%Y %H:%M:%S")
                        sw.write(f"{user['userId']},{now},{lastSeen_norm},{user['isOnline']}\n")
                        
    elif command == "2":
        total = 200
        phrases = []

        print("Яку мову хочете обрати/What language you want to choose: 1 - Українська, 2 - English")
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
                    print(f"{user['nickname']} {phrases[15]} {status}")

    elif command == "3":
        path = check()
        GetHistory(path)

    elif command == "4":
        path = check()
        GetHistorySpec(path)

    elif command == "5":
        path = check()
        GetPrediction(path)
    elif command == "6":
        path = check()
        GetPredictionUser(path)

if __name__ == "__main__":
    main()
