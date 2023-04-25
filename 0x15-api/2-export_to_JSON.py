#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:48:00 2023
@author: Phylis Mercy
"""
from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dictionary, file)
