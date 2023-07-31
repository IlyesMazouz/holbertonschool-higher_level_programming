#!/usr/bin/python3

"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = conn.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    city_names = ", ".join(city[0] for city in results)
    print(city_names)

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

    filter_cities_by_state(mysql_username, mysql_password, database_name, state_name)
