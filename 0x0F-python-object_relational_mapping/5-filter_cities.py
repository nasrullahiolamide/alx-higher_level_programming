#!/usr/bin/python3

"""
print all cities by state
"""

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
        WHERE states.name LIKE '{:s}'
        '''.format(argv[4])
    )

    print(', '.join(r[1] for r in cursor.fetchall()))
    cursor.close()
    db.close()
