#!/usr/bin/python3
"""Create CSV file"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for t in tasks:
        with open("{}.csv".format(sys.argv[1]), mode='a') as f:
            writer = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL
            )

            writer.writerow(
                    [str(sys.argv[1]),
                    str(user.get('username')),
                    str(t.get("completed")),
                    str(t.get("title"))]
                    )
