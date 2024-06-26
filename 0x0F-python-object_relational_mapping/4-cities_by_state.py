#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> "
        "<db_name>".format(sys.argv[0]))
        sys.exit(1)

    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=mysql_username, passwd=mysql_password,
                             db=db_name)
        cursor = db.cursor()

        # Prepare SQL query to fetch cities with state names
        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC
                """

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database or executing "
        "query: {}".format(e))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

