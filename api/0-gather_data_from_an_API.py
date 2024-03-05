#!/usr/bin/python3
"""
returns information about his/her todo list progress
"""

import sys
import requests

if __name__ == "__main__":
    BASE_URL = "https://jsonplaceholder.typicode.com/users"
    try:
        user_info_response = requests.get(f'{BASE_URL}/{sys.argv[1]}',
                                          timeout=5000)
        todos_response = requests.get(f'{BASE_URL}/{sys.argv[1]}/todos',
                                      timeout=5000)

        todos = todos_response.json()
        user_info = user_info_response.json()
        user_name = user_info["name"]
        total_task = len(todos)
        completed_tasks = []

        for todo in todos:
            if todo["completed"] is True:
                completed_tasks.append(todo["title"])

        print(f"Employee {user_name} is done with tasks"
              f"({len(completed_tasks)}/{total_task}):")
        for completed_task in completed_tasks:
            print("\t"+completed_task)
    except IndexError:
        print("Invalid id")
