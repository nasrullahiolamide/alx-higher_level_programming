#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        '''
        SELECT cities.id, cities.name, states.name
        from cities
        JOIN states ON cities.state_id = states.id
        '''
    )

    for r in cursor.fetchall():
        print(r)

    cursor.close()
    db.close()
