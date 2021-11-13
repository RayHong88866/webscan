from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DbModel():
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
     
class target(db.Model, DbModel):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(256), index=True)
    scount = db.Column(db.Integer, default=0)
    status = db.Column(db.String(10))
    addtime = db.Column(db.DateTime,default=datetime.now)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
       
    def __init__(self, domain,scount, status, starttime = None, endtime=None):
        self.domain = domain
        self.scount = scount
        self.status = status
        self.starttime = starttime
        self.endtime = endtime
        
    

class subdomains(db.Model, DbModel):
    id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, index=True)
    name = db.Column(db.String(256))
    
    def __init__(self, target_id, name):
        self.target_id = target_id
        self.name = name
    
    