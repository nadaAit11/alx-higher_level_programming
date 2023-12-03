#!/usr/bin/python3
"""Retrieve and display X-Request-Id variable from URL"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
