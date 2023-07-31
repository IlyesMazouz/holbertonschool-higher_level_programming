#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def get_states(username, password, database):
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

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

    get_states(mysql_username, mysql_password, database_name)
