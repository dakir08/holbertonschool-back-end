#!/usr/bin/python3
"""
returns information about his/her todo list progress
"""

import requests

if __name__ == "__main__":

    x = requests.get('https://jsonplaceholder.typicode.com/todos')

    response = x.json()
    print(response)
