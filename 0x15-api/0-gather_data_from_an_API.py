#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + "users/" + str(employee_id)
    user_response = requests.get(user_url)
    if user_response.ok:
        employee_name = user_response.json().get('name')

        todos_url = base_url + "todos?userId=" + str(employee_id)
        todos_response = requests.get(todos_url)
        if todos_response.ok:
            todos = todos_response.json()

            total_tasks = len(todos)
            completed_tasks = sum(task['completed'] for task in todos)
            completed_task_titles = \
                [task['title'] for task in todos if task['completed']]

            print(f"Employee {employee_name} is \
done with tasks({completed_tasks}/{total_tasks}):")
            for title in completed_task_titles:
                print("\t " + title)
