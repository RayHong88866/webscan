import sqlite3
from module.gobuster import gobuster

def db_init():
    conn =  sqlite3.connect('db/db.sqlite')
    return conn

def scan():
    conn =  db_init()
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM target where status='queue'"):     
        print(f'scan : {row[1]}')  
        print(gobuster.dns(row[1]))
        f = open(f'module/goscan/{row[1]}_dns.txt')
        print(row[0])
        cur.execute('delete from subdomains where target_id=?',str(row[0]))
        conn.commit()
        line = f.readline()
        count = 1
        while line:
            #print(line)
            cur.execute('insert into subdomains(target_id, name)  values(?,?)',(row[0], line.split(':')[1].strip()))
            line = f.readline()
            count +=1
            conn.commit()
        cur.execute("update target set status='gobuster',scount=? where id=?",(str(count) ,str(row[0])))
        conn.commit()
   
   

scan()