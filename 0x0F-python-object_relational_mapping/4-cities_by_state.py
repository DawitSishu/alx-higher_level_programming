#!/usr/bin/python3
"""
all cities
"""

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    nme = sys.argv[3]

    # defalt port - 3306
    db = MySQLdb.connect(user=usr, passwd=pas, db=nme)
    curs = db.cursor()

    curs.execute("SELECT c.id, c.name, s.name \
                 FROM cities c INNER JOIN states s \
                 ON c.state_id = s.id \
                 ORDER BY c.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
