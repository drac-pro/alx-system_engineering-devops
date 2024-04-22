#!/usr/bin/python3
"""export data in the CSV format"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get('username')
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open('{}.json'.format(user_id), 'w') as jsonout:
        json.dump({user_id: [{
                  'task': task.get('title'),
                  'completed': task.get('completed'),
                  'username': username
                  } for task in todos]}, jsonout)
