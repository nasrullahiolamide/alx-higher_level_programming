#!/usr/bin/python3
"""
return states tht starts with 'N'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # connect to db
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Create cursor to work in db
    cursor = db.cursor()

    cursor.execute(
        'SELECT * from states WHERE name LIKE \'N%\' ORDER BY id ASC')
    for r in cursor.fetchall():
        if r[1][0] == 'N':
            print(r)
    cursor.close()
    db.close
