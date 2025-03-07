#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
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
    
    # Fetch all results
    query_rows = cur.fetchall()
    
    # Print results row by row
    for row in query_rows:
        print(row)
    
    # Close cursor and connection
    cur.close()
    conn.close()

