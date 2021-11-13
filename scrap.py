import requests as req
import sqlite3
from lxml import etree
from requests.models import Response


url = 'https://hedb.moe.edu.tw/uni.html'
conn =  sqlite3.connect('db/db.sqlite')
cur = conn.cursor()

response = req.get(url).text
#print(response)
html = etree.HTML(response)
domain =''
for href in html.xpath('//tr/td/a/@href'):
    try:
        href = href.split('/')[2].split('.')[1:]
        domain='.'.join(href)
        print(domain)
        cur.execute('insert into target(domain, status) values(?,?)',(domain, 'queue'))
        
    except:
        pass

conn.commit()
conn.close()