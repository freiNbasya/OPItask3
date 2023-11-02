import json
import requests
from pathlib import Path
from datetime import datetime
import pandas as p
import os

def get_users(offset, base_url):
    params = {"offset": offset}
    response = requests.get(base_url, params=params)
    content = response.text
    users_response = json.loads(content)

    return users_response


def printList(url):
    total = 200
    output_file = Path("main/list.csv")
    file = "list.csv"
    if output_file.exists():
        df = p.read_csv(output_file)
        print(df)
    else:
        with output_file.open(mode="w", encoding="utf-8") as sw:
            sw.write("username,userId,firstSeen\n")
            for i in range(0, total, 20):
                users_response = get_users(i, url)
                total = users_response["total"]
                now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                for user in users_response["data"]:
                    if user['isOnline']:
                        sw.write(f"{user['nickname']},{user['userId']},{now}\n")
                    else:
                        firstSeen = datetime.fromisoformat(user['lastSeenDate'])
                        firstSeen_norm = firstSeen.strftime("%d-%m-%Y %H:%M:%S")
                        sw.write(f"{user['nickname']},{user['userId']},{firstSeen_norm}\n")
                        df = p.read_csv("main\list.csv")
                        print(df)
    

    return "Dataset successfuly printed"