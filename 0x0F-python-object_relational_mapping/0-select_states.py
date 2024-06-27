#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to a MySQL server and lists all states from the database
    hbtn_0e_0_usa.

    Args:
        username (str): 'root'
        password (str): 'root'
        database (str): 'hbtn_0e_0_usa'

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
