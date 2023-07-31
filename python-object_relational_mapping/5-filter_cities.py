#!/usr/bin/python3

"""a script that takes in the name of a state as an argument 
and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_username> <mysql_password> <database_name>".format(
                sys.argv[0]
            )
        )
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_cities_by_state(mysql_username, mysql_password, database_name)
