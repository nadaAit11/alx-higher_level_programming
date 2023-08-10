#!/usr/bin/python3
# Print the result of the addition of all arguments

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    result = 0

    for arg in args:
        result += int(arg)

    print(result)
