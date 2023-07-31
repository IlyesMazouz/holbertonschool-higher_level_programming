#!/usr/bin/python3

"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(
        state_name
    )

    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states_by_name(mysql_username, mysql_password, database_name, state_name)
