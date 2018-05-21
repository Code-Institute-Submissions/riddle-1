import os
from flask import Flask, url_for
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask import Flask, flash, redirect, render_template, request, session
from flask import abort
from flask import Session
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import json
import random


app = Flask(__name__)
engine = create_engine('sqlite:///riddle.db', echo=True)


def load_data():
    data = json.load(open('riddles.json'))
    return data

data = load_data()


def check_answer(id, result):
    return result.lower() == data[id]['answer'].lower()


def add_user(user, passw):
    Session = sessionmaker(bind=engine)
    s = Session()
    new_user = User(username=user, password=passw, answers=int(0))
    s.add(new_user)
    s.commit()


def get_userdb(usern):
    Session = sessionmaker(bind=engine)
    s = Session()
    r = s.query(User).filter_by(username=usern)
    result = None
    if r:
        result = r.first()
    return result


def get_userdb_p(user, passw):
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter_by(username=user, password=passw)
    result = None
    if query:
        result = query.first()
    return result


def drop_userdb(user):
    Session = sessionmaker(bind=engine)
    s = Session()
    r = s.query(User).filter_by(username=user)
    if r:
        result = r.first()
        if result:
            s.delete(result)
    s.commit()


@app.route('/')
def home():
    if not session.get('logged_in'):
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User)
        return render_template('login.html', query=query)
    else:
        size = len(data)
        randomq = random.randint(0, size-1)
        result = get_userdb(session['user'])
        return render_template('riddle.html', data=data[randomq],
                               id=randomq, correct=result.answers)


@app.route("/action", methods=['POST'])
def action():
    result = request.form.get("result")
    id = int(request.form.get("id"))
    rw = ''
    if check_answer(id, result):
        rw = "Correct"
        Session = sessionmaker(bind=engine)
        s = Session()
        our_user = s.query(User).filter_by(username=session['user']).first()
        our_user.answers += 1
        s.commit()
    else:
        rw = "Incorrect"
    return render_template('answer.html', rw=rw, answer=data[id]['answer'])


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    result = get_userdb_p(POST_USERNAME, POST_PASSWORD)
    if result:
        session['logged_in'] = True
        session['user'] = POST_USERNAME
    else:
        return ('Wrong password <a href=\'/\'>Try again</a>')
    return home()


@app.route('/register', methods=['POST'])
def do_admin_register():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    result = get_userdb(POST_USERNAME)
    if result:
        return('Name taken <br><a href=\'/\'>Try again</a>')
    else:
        add_user(POST_USERNAME, POST_PASSWORD)
        return('Username created <br><a href=\'/\'>Login</a>')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


app.secret_key = os.urandom(12)


