#!/usr/bin/python3
"""
filter states by n
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

    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
