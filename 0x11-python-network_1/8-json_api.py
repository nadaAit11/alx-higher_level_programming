#!/usr/bin/python3
"""
Send a POST request with a letter parameter and handle JSON response
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    response = requests.post(
        'http://0.0.0.0:5000/search_user', data=payload
    )

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'), json_response.get('name')
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
