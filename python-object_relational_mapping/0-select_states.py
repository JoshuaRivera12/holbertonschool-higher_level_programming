#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute SQL query
        cur.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # Clean up
        cur.close()
        conn.close()

    except MySQLdb.OperationalError as e:
        print("Database connection failed:", e)
        sys.exit(1)

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
