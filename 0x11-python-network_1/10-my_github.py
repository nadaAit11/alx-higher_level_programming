#!/usr/bin/python3
"""
Displays a user's GitHub ID using Basic Authentication and GitHub API
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
