#!/usr/bin/python3
"""A script that pulls employee TODO list using REST API."""

import csv
import requests
from sys import argv


def fetch_user_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None

    if "id" not in user_data:
        print(f"User with ID {employee_id} not found.")
        return None, None

    return user_data, todos_data


def export_to_csv(employee_id, user_data, todos_data):
    if not user_data or not todos_data:
        return

    user_id = user_data["id"]
    username = user_data["username"]
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': 'COMPLETED'if task['completed'] else
                'NOT COMPLETED',
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./export_to_csv.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    user_data, todos_data = fetch_user_data(employee_id)
    export_to_csv(employee_id, user_data, todos_data)
