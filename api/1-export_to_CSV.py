#!/usr/bin/python3
"""
export to CSV
"""

import csv
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    try:
        user_info_response = requests.get(f'{base_url}/{sys.argv[1]}')
        todos_response = requests.get(f'{base_url}/{sys.argv[1]}/todos')

        todos = todos_response.json()
        user_info = user_info_response.json()
        id = user_info["id"]
        user_name = user_info["username"]
        total_task = len(todos)
        completed_tasks = []

        for todo in todos:
            if todo["completed"] is True:
                completed_tasks.append(todo["title"])

        with open(f'{id}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for task in todos:
                file.write(f'"{id}","{user_name}",'
                           f'"{task["completed"]}","{task["title"]}"')
                file.write('\n')
    except IndexError:
        print("Invalid id")
