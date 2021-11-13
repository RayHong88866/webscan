from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain= db.Column(db.String(256), index=True)
    
    def __init__(self, domain):
        self.domain = domain

