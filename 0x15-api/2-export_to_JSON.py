#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json

Example:
"""
import json
import requests
import sys

if __name__ == "__main__":
    _id = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(_id)).json().get("username")
    _tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(eid)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = username
            _tasks.append(temp)

    with open("{}.json".format(eid), 'w+') as jsonfile:
        json.dump({eid: _tasks}, jsonfile)
