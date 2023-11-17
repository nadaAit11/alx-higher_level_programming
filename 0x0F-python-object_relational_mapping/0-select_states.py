#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve the list of states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and display the results
    states = cursor.fetchall()
    for s in states:
        print(s)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states(username, password, database)
