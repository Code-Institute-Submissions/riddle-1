import os
from flask import Flask, url_for
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Session
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json
import random


app = Flask(__name__)
engine = create_engine('sqlite:///tutorial.db', echo=True)

data = []
@app.route('/')
def home():
    if not session.get('logged_in'):
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User)
        return render_template('login.html', query=query)
    else:
        global data
        data = json.load(open('riddles.json'))
        size = len(data)
        randomq = random.randint(0,size-1)
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([session['user']]))
        result = query.first()
        return render_template('riddle.html', data=data[randomq], id=randomq, correct=result.answers)

@app.route("/action", methods=['POST'])
def action():
	result = request.form.get("result")
	id = int(request.form.get("id"))
	rw = ''
	if result == data[id]['answer']:
	    rw = "Correct"
	    Session = sessionmaker(bind=engine)
	    s = Session()
	    	
	    
	    our_user = s.query(User).filter_by(username=session['user']).first() 
	    print(our_user.answers)
	    our_user.answers += 1
	    
	    s.commit()
	else:
	    rw =  "Incorrect"
	    
	return render_template('answer.html', rw=rw, answer = data[id]['answer'])


@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        session['user'] = POST_USERNAME
       
    else:
        return ('Wrong password <a href=\'/\'>Try again</a>');
    return home()
 
@app.route('/register', methods=['POST'])
def do_admin_register():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    #query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    #result = query.first()
    
    query = s.query(User).filter(User.username.in_([POST_USERNAME]))
    result = query.first()

    if result:
        return('Name taken <br><a href=\'/\'>Try again</a>')
    else:
        new_user = User(username=POST_USERNAME, password=POST_PASSWORD, answers=int(0))
        s.add(new_user)
        s.commit()
        return('Username created <br><a href=\'/\'>Login</a>')
    return home()
    
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


app.secret_key = os.urandom(12) 
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

