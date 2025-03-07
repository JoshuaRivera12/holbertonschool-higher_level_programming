#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object to interact with the database
        cur = conn.cursor()

        # Execute SQL query to retrieve all states sorted by id
        cur.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch and print results
        for row in cur.fetchall():
            print(row)

        # Clean up
        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
        sys.exit(1)

