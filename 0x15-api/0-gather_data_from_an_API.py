#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'user/{}'.format(argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    completed = [task.get('title') for task in todos if task.get('completed')
                 is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed), len(todos)))
    [print('\t {}'.format(c)) for c in completed]
