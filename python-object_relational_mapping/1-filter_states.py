#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
    db=sys.argv[3], port=3306)    

    # Creating Cursor
    cursor = db.cursor()

    # Execute SQL Query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print result
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close
