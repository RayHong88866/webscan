import sqlite3
from module.gobuster import gobuster

def db_init():
    conn =  sqlite3.connect('db/db.sqlite')
    return conn

def scan():
    conn =  db_init()
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM target where status='queue'").fetchall()
    
    for row in rows:     
        print(f'scan : {row[1]}')  
        gobuster.dns(row[1])
        f = open(f'module/goscan/{row[1]}_dns.txt')
        #print(row[0])
        #cur.execute('delete from subdomains where target_id=?',str(row[0]))
        #print('delete ...')
        line = f.readline()
        count = 0
        while line:
            print('insert '+line)
            
            cur.execute('insert into subdomains(target_id, name)  values(?,?)',(row[0], line.split(':')[1].strip()))
            line = f.readline()
            count +=1
            
        if count >0:
            print('update ...')
            cur.execute("update target set status='gobuster',scount=? where id=?",(str(count) ,str(row[0])))
            conn.commit()
    conn.close()
   

scan()

#conn =  sqlite3.connect('db/db.sqlite')
#cur = conn.cursor()
#rows = cur.execute("SELECT * FROM target where status='queue'")
#print(rows.fetchall())