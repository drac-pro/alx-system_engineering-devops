#!/usr/bin/python3
"""export data in the CSV format"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get('username')
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open('{}.csv'.format(user_id), 'w', newline="") as csvout:
        writer = csv.writer(csvout, quoting=csv.QUOTE_ALL)
        for task in sorted(todos):
            writer.writerow([user_id, username,
                            task.get('completed'), task.get('title')])
