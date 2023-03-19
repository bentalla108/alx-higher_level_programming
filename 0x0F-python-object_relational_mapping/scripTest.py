#!/usr/bin/python3
"""List states -  Module"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3333,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY
                    states.id ASC""",)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()