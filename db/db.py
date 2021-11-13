from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(256), index=True)
    status = db.Column(db.String(10))
    addtime = db.Column(db.DateTime,default=datetime.now)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
       
    def __init__(self, domain, status, starttime = None, endtime=None):
        self.domain = domain
        self.status = status
        self.starttime = starttime
        self.endtime = endtime
        
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
     
