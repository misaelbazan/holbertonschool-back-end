#!/usr/bin/python3
"""This module contains the script for the 0th task"""

import csv
import requests
import sys


def list_completed_tasks(todo_data):
    """Count n of completed tasks"""
    return [task for task in todo_data if task["completed"]]

def get_todo_list_titles(todo_data):
    return [task['title'] for task in todo_data]

def todo_list_task_status(todo_data):
    return [task['completed'] for task in todo_data]

def save_to_csv(filename, employee_todos):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(employee_todos)

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

        todos_list_status = todo_list_task_status(todos_data)
        todos_titles = get_todo_list_titles(todos_data)
        employee_todos = []
        for index in range(0, TOTAL_NUMBER_OF_TASKS):
            record = [str(id), EMPLOYEE_NAME, str(
                todos_list_status[index]), todos_titles[index]]
            employee_todos.append(record)

        csv_file_name = f"{id}.csv"
 
        save_to_csv(csv_file_name, employee_todos)

    except requests.RequestException as e:
        print("Error happened during execution", e)


if __name__ == "__main__":
    main()
