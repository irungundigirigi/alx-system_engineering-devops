#!/usr/bin/python3
"""Generate a Todo list for a given employee id and export to JSON"""
import requests
import json
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]

    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks = [{"task": i["title"], "completed": i["completed"], "username": user["username"]} for i in todos]

    result = {user_id: tasks}

    # Write to JSON file
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(result, json_file, indent=4)

    print(f"Employee {user.get('name')} is done with tasks({len(tasks)}/{len(todos)}).")
    print(f"Exported to {filename}")
