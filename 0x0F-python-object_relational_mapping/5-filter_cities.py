#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state.
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

        # Prepare SQL query to fetch cities of the specified state
        query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """

        # Execute the query with the safe method by passing the parameter
        #separately
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Display results
        cities = [row[0] for row in results]
        print(", ".join(cities))

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
