#!/usr/bin/python3
""" Json """
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


def outputJson(edUser, todoUser):
    """ Print the output """

    dictJson = dict()
    dictin = dict()
    listdict = []
    username = edUser[0]["username"]
    for i in range(len(todoUser)):
        dictin = dict()
        dictin["task"] = todoUser[i]["title"]
        dictin["completed"] = todoUser[i]["completed"]
        dictin["username"] = username
        listdict.append(dictin)

    dictJson[edUser[0]["id"]] = listdict
    with open("{}.json".format(edUser[0]["id"]), mode='w') as f:
        f.write(json.dumps(dictJson))


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

    outputJson(edUser, todoUser)
