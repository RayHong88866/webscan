from flask import Flask, render_template, request, redirect, url_for
from db.db import db,target,subdomains

app = Flask(__name__)
    

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()
db.create_all()

@app.route('/')
def index():
    db.create_all()
    targets = target.query.all()  
    return render_template('index.html',targets=targets)

@app.route('/target_add',methods = ['POST'])
def add():
    target(domain = request.form.get('target'), status='queue').add()
    return  redirect('/')

@app.route('/target_del/<id>')
def delete(id):
    t = target.query.filter_by(id = id)
    t.delete()
    #db_func.option.delete(id)
  
    return  redirect('/')

@app.route('/dns/<target_name>/<id>')
def dns_page(target_name, id):
    t = subdomains.query.filter_by(target_id=id).all()
    print(t)
    return render_template('dns.html', subdomains=t, domain=target_name)