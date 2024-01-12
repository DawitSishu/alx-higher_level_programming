#!/usr/bin/python3
"""
list all stattrs
"""

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    nme = sys.argv[3]

    # defalt port - 3306
    db = MySQLdb.connect(user=usr, passwd=pas, db=nme)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
