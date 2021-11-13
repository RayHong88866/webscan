import sqlite3
from module.gobuster import gobuster

def db_init():
    conn =  sqlite3.connect('db/db.sqlite')
    return conn.cursor()

def scan():
    cur =  db_init()
    for row in cur.execute("SELECT * FROM target where status='queue'"):     
        print(f'scan : {row[1]}')  
        print(gobuster.dns(row[1]))
            


scan()