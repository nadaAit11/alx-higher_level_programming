#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

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

    # Fetch all rows and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Disconnect from server
    db.close()


if __name__ == "__main__":
    # Retrieve arguments from command line
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
