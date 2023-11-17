#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database
    )

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    y Fetch all rows and display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Disconnect from server
    db.close()


if __name__ == "__main__":
    # Retrieve arguments from command line
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, database)
