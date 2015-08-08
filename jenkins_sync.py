import jenkins
import sqlite3
import sys

jen = jenkins.Jenkins('http://128.199.185.100:8080/', 'jenkins', 'jenkins')
jobs = jen.get_jobs()

i = 0
jobs_data = list()

for jb in jobs:
    i = i+1
    jobs_data.append([i, jb.get('name'), jb.get('color')])

try:
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    cur.execute("DELETE FROM jenkinsapp_jobs")
    cur.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='jenkinsapp_jobs'")
    cur.executemany("INSERT INTO jenkinsapp_jobs VALUES(?, ?, ?)", jobs_data)

    con.commit()

except sqlite3.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
