import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from questionPack import qBank
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_mail import Mail, Message
from decouple import config
from helpers import login_required, mark
import random
import json
from formParser import formparser,getInitialList,getFinalList
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# # configure SQLITE
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
class users(db.Model):

    id = db.Column('user_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    hash_ = db.Column(db.String(50))  
    email = db.Column(db.String(200))

    def __init__(self, username, hash_, email):
        self.username = username
        self.hash_ = hash_
        self.email = email

db.create_all()

# API key 
app.secret_key = config('secret_key')

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Flask mail configuration

app.config['MAIL_SERVER']=config('MAIL_SERVER')
app.config['MAIL_PORT'] = int(config('MAIL_PORT'))
app.config['MAIL_USERNAME'] = config('EMAIL')
app.config['MAIL_PASSWORD'] = int(config('PASSWORD'))
app.config['MAIL_USE_TLS'] =False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



# ROUTES START

@app.route("/")
# @login_required
def index():
    return render_template("index.html")

@app.route("/history")
# @login_required
def history():
    message="These are the users"
    return render_template("showAll.html", message= "message", users = users.query.all())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # Fetch the username from the table which comes in a form of list of objects(one object in this case[0])
        result = users.query.filter_by(username = username).all()

        # Ensure username was submitted
        if not username:
            flash('Enter your username', 'error')
        # Ensure password was submitted
        elif not password:
            flash('Must provide password', 'error')
        elif not result:
            flash('User not registered', 'error')
            return redirect("/login")


        rows = result[0]
        user_id_ = rows.id
        # Ensure username exists and password is correct
        if not result or not check_password_hash(rows.hash_, password):
            flash('Username/password incorrect', 'error')

       
        # Remember which user has logged in
        session["user_id"] = user_id_

        # Else Redirect user to dashboard
        return redirect("/dashboard")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username =  request.form['username']
        password = request.form['password']
        email = request.form['email']
        confirmation = request.form['confirmation']

        # Query the table users for username and email, then store them in a variable
        user_check = users.query.filter_by(username = username).all()
        email_check = users.query.filter_by(username = email).all()

        if not username or not password or not email:
            flash('Please enter all the fields', 'error')
        elif len(password) <= 5:
            flash('Password too short', 'error') 
        elif not password == confirmation:
            flash('Passwords do not match', 'error')
        elif len(user_check) != 0:
            flash('Username already exists', 'error')
        elif len(email_check) != 0:
            flash('Email already exists', 'error')
        else:
            hash_ = generate_password_hash(password)
            user = users(username, hash_, email)
         
            db.session.add(user)
            db.session.commit()
         
            flash('Registration successful')
            
            msg = Message('Hello', sender = config('EMAIL'), recipients = [email])
            msg.body = "Thank you for joining Rookie Hub, good luck with your adventure :)"
            mail.send(msg)

            return redirect("/login", 302)
    return render_template("register.html")



@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")



@app.route('/questions')
@login_required
def question():
    return render_template('questions.html',qBank= qBank, question=0, value=0)

@app.route('/question-me', methods=["POST","GET"])
@login_required
def question_me():
    if request.method=="POST":
        results = request.get_json()
        score = mark(results)
    return render_template('congratulations.html', score=score)

@app.route('/generate-questions', methods=["POST","GET"])
# @login_required
def generate_questions():
    if request.method=="POST":
        topic,questions,options,correctAnwer = formparser(request)
        answers,questionsSmallBatch = getInitialList(questions,options,correctAnwer,realOptions=[],answersList=[])
        print(questionsSmallBatch)

        # questionToPersist = {
        #     topic:bigOptionList,
        #     topic+'Answers':correctAnwer
        # }
        return render_template('questionGetter.html')
    if request.method == "GET":
        return render_template('questionGetter.html')
                
        
       
