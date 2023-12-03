#!/usr/bin/python3
"""
Send a request to a URL and display the response body.
If HTTP status code >= 400, print Error code: followed by the code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
