#!/usr/bin/python3
""" A JSONPlacholder to get employee data """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()
    user_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        user_task.append(dict_task)

    final_task = {str(userid): user_task}
    filename = '{}.json'.format(userid)
    with open(filename, mode='w') as f:
        json.dump(final_task, f)
