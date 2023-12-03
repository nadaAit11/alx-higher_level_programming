#!/usr/bin/python3
"""
Send a POST request to a provided URL with an email parameter
"""

import requests
import sys

if __name__ == '__main__':
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(sys.argv[1], data=payload)
    print(response.text)
