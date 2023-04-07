#!/usr/bin/python3
""" api """
import requests
import sys


def check(request):
    """ check the request """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())

def output(edUser, todoUser):
    """ Print the output """

    if len(edUser) != 0:
        EMPLOYEE_NAME = edUser[0]["name"]
    else:
        EMPLOYEE_NAME = "Not found"
    NUMBER_OF_DONE_TASKS = str(todoUser).count('\'completed\': True')
    TOTAL_NUMBER_OF_TASKS = len(todoUser)

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in todoUser:
        if task["completed"]:
            print("\t {}".format(task["title"]))
    

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

    output(edUser, todoUser)
