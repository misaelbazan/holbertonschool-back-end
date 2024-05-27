#!/usr/bin/python3
"""This module contains the script for the 0th task"""

import requests
import sys


def list_completed_tasks(todo_data):
    """Count n of completed tasks"""
    return [task for task in todo_data if task["completed"]]


def main():
    id = sys.argv[1]
    try:
        # Fetching user data
        user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetching todos data
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        EMPLOYEE_NAME = user_data['name']
        completed_tasks = list_completed_tasks(todos_data)
        NUMBER_OF_DONE_TASKS = len(completed_tasks)
        TOTAL_NUMBER_OF_TASKS = len(todos_data)

        print(f"Employee {EMPLOYEE_NAME} is done with tasks\
            ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in completed_tasks:
            TASK_TITLE = task['title']
            print(f"\t{TASK_TITLE}")
    except requests.RequestException as e:
        print("Error happened during execution", e)


if __name__ == "__main__":
    main()
