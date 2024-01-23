#!/usr/bin/python3
""" A JSONPlacholder to get employee data """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users = '{}users/'.format(url)
    res = requests.get(users)
    json_o = res.json()
    final_task = {}
    for u in json_o:
        name = u.get('username')

        todos = '{}todos?userId={}'.format(url, u.get('id'))
        res2 = requests.get(todos)
        tasks = res2.json()
        user_task = []
        for task in tasks:
            dict_task = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": name}
            user_task.append(dict_task)

        final_task[str(u.get('id'))] = user_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='a') as f:
        json.dump(final_task, f)
