#!/usr/bin/python3

"""Displays all values in the states table where name matches the argument (safe from SQL injection)"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

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
