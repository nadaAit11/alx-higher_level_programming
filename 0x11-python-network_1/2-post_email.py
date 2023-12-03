#!/usr/bin/python3
"""
Send a POST request to a given URL with an email as a parameter
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {'email': email}
    data = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')

    print(response_data)
