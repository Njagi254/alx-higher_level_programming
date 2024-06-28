#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <db_name> "
              "<state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=mysql_username, passwd=mysql_password,
                             db=db_name)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        sys.exit(1)

    # Prepare SQL query
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute the query
    try:
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error executing MySQL query: {}".format(e))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()
