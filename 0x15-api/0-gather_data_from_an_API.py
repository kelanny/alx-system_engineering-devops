#!/usr/bin/python3
"""A script that pulls employee TODO list using REST API."""

import requests
import sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./gather_data_from_API.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        exit(1)

    employee_name = user_data["name"]
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    print(f"Employee {employee_name} is done with tasks \
            ({num_completed_tasks}/{total_tasks})")
    for task in completed_tasks:
        print(f"\t {task['title']}")
