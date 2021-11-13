from flask import app
from flask_sqlalchemy  import SQLAlchemy
from ..run import app

db = SQLAlchemy(app)

class target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain= db.Column(db.String(256), index=True)


db.create_all()
class option():
   
    def add(target):   
        try:    
            db.session.add(target(domain=target))
            db.session.commit()
        except:
            return -1

        return 0

    def delete(id):
        try:
            dele = target.query.filter_by(id=id).first()
            db.session.delete(dele)
            db.session.commit()
        except:
            return -1
        
        return 0



