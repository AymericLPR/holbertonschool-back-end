#!/usr/bin/python3
""" dict """
import json
import requests
import sys


def check(request):
    """ check the request """
    print(request)
    print(request.status_code)
    print(request.headers)
    print(request.text)
    print(request.json())


def outputDick(edUser, todoUser):
    """ Print the output """
    # Output Preparation
    dictJson = dict()
    dictin = dict()
    listdict = []
    for user in edUser:
        listdict = []
        for task in todoUser:
            dictin = dict()
            if task["userId"] == user["id"]:
                dictin["username"] = user["username"]
                dictin["task"] = task["title"]
                dictin["completed"] = task["completed"]
                listdict.append(dictin)
        dictJson[user["id"]] = listdict

    with open("todo_all_employees.json", mode='w') as f:
        f.write(json.dumps(dictJson))


userLink = "https://jsonplaceholder.typicode.com/users/"
requestPerson = requests.get(userLink)

todoLink = "https://jsonplaceholder.typicode.com/todos/"
requesttodo = requests.get(todoLink)

edUser = requestPerson.json()
todoUser = requesttodo.json()

outputDick(edUser, todoUser)
