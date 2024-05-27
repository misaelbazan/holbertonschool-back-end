#!/usr/bin/python3
"""This module contains the script for the 0th task"""

import requests
import sys


def list_completed_tasks(todo_data):
    """Count n of completed tasks"""
    return [task for task in todo_data if task["completed"]]


try:
    employee_id = sys.argv[1]
    # Fetching user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetching todos data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId=\
                {employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    completed_tasks = list_completed_tasks(todos_data)
    number_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    print(f"Employee {user_data['name']} is done with tasks\
         ({number_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}") 
except:
    print("Error happened during execution")
