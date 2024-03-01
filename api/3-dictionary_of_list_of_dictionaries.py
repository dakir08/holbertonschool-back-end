#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    data = {}
    try:
        user_infos_response = requests.get(f'{base_url}/')
        user_infos = user_infos_response.json()

        for user_info in user_infos:
            todos_response = requests.get(f'{base_url}/{user_info["id"]}/todos')

            todos = todos_response.json()
            id = user_info["id"]
            user_name = user_info["username"]
            total_task = len(todos)
            completed_tasks = []

            for todo in todos:
                if todo["completed"] is True:
                    completed_tasks.append(todo["title"])
            
            data[id] = []

            for task in todos:
                data[id].append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_name
                })

            with open(f'todo_all_employees.json', 'w') as f:
                json.dump(data, f)
    except IndexError:
        print("Invalid id")
