from flask import Flask, render_template, request, redirect, url_for
from db.db import db,target


app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.create_all()
@app.route('/')
def index():
    targets = target.query.all()  
    return render_template('index.html',targets=targets)

@app.route('/target_add',methods = ['POST'])
def add():
    db.session.add(target(request.form.get('target')))
    db.session.commit()
    return  redirect('/')

@app.route('/target_del/<id>')
def delete(id):
    #db_func.option.delete(id)
  
    return  redirect('/')