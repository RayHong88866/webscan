from flask import Flask, render_template, request, redirect, url_for
from models.Target import *

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def index():
    targets = target.query.all()
    return render_template('index.html',targets=targets)

@app.route('/target_add',methods = ['POST'])
def add():
    option.add(request.form.get('target'))   
    return  redirect('/')

@app.route('/target_del/<id>')
def delete(id):
    option.delete(id)
  
    return  redirect('/')