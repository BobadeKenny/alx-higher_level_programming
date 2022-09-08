#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT name FROM cities
                 WHERE state_id=(SELECT id FROM states WHERE name=%s)
                  ORDER BY id""",
                [argv[4]])
    rows = cur.fetchall()
    for row in rows:
        print(row[0], end=", " if rows[-1] != row else "\n")
    cur.close()
    db.close()
