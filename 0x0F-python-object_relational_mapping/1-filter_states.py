#!/usr/bin/python3
"""
Module to list all states with a name starting with 'N' from a given database.
"""

import MySQLdb
import sys


def list_states_starting_with_n(mysql_username, mysql_password, db_name):
    """
    Connects to a MySQL database and lists all states with a name
    starting with 'N'.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        db_name (str): The name of the database.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states with names starting
    # with 'N' sorted by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # Print each state in the specified format
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main entry point of the script. Parses command-line arguments and calls
    the function
    to list states starting with 'N'.
    """
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> <mysql_password> "
              f"<db_name>")
        sys.exit(1)

    # Get MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # List states starting with 'N'
    list_states_starting_with_n(mysql_username, mysql_password, db_name)
