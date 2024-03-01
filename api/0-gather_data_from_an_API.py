#!/usr/bin/python3
"""
returns information about his/her todo list progress
"""

import sys
import requests

if __name__ == "__main__":

    try:
        user_info_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')

        todos = todos_response.json()
        user_info = user_info_response.json()
        user_name = user_info["name"]
        total_task = len(todos)
        completed_tasks = []

        for todo in todos:
            if todo["completed"] is True:
                completed_tasks.append(todo["title"])
        
        print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_task}):")
        for completed_task in completed_tasks:
            print("\t"+completed_task)
    except IndexError:
        print("Invalid id")
