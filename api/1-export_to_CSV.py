#!/usr/bin/python3
""" CVS """
import csv
import requests
import sys


def check(request):
    """ check the request """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())


def outputCVS(edUser, todoUser):
    """ Print the output """

    with open("{}.csv".format(edUser[0]["id"]), mode='w') as f:
        tasks = csv.writer(f, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL)

        for task in todoUser:
            tasks.writerow([edUser[0]["id"],
                            edUser[0]["username"],
                            task["completed"],
                            task["title"]])


if len(sys.argv) == 2:
    userLink = "https://jsonplaceholder.typicode.com/users/"
    id = sys.argv[1]
    queryUser = {'id': id}
    requestPerson = requests.get(userLink, params=queryUser)

    todoLink = "https://jsonplaceholder.typicode.com/todos/"
    querytodo = {'userId': id}
    requesttodo = requests.get(todoLink, params=querytodo)

    edUser = requestPerson.json()
    todoUser = requesttodo.json()

    outputCVS(edUser, todoUser)
