import subprocess
import sqlite3

from db.db import target
class gobuster():


    def dns(target_name, target_id, dir_path='/home/ray/work/webscan/SecLists/Discovery/DNS/subdomains-top1million-5000.txt'):
        conn = sqlite3.connect('db/db.sqlite')
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM target where status='queue' and domain = ?", str(target_name)).fetchall()
        if rows.count == 0:
            return 'finished'

        cur.execute("update target set status='dnsing' where domain=?", (target_name))
        conn.commit()
        save_path = f'/home/ray/work/webscan/module/goscan/{target_name}_dns.txt'
        with subprocess.Popen(['/bin/gobuster', 'dns', '-w', dir_path,
                               '-d', target_name, '-o', save_path , '-q' ], stdout=subprocess.PIPE) as proc:
            if b'finshed' in proc.stdout.read():                                                    
                f = open(save_path)        
                line = f.readline()
                count = 0
                while line:
                    print('insert '+line)            
                    cur.execute('insert into subdomains(target_id, name)  values(?,?)',(target_id, line.split(':')[1].strip()))
                    line = f.readline()
                    count +=1            

                if count >0:
                    print('update ...')
                    cur.execute("update target set status='gobuster',scount=? where id=?",(str(count) ,str(target_id)))
                    conn.commit()

                cur.execute("update arget set status='dnsfinish' where domain= ?", (target_name))
                return 'finshed'
    
    def dir(target_name, dir_path, ext):
        with subprocess.Popen(['/bin/gobuster', 'dir', '-w', dir_path,
                               '-u', target_name, '-o', f'/home/ray/work/webscan/module/goscan/{target_name}_dir.txt', '-q'], stdout=subprocess.PIPE) as proc:
            if b'finshed' in proc.stdout.read():
                proc.kill()
        
#gobuster.dns('test', '/home/ray/work/webscan/SecLists/Discovery/DNS/namelist.txt')