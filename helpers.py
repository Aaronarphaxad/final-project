from flask import redirect, render_template, request, session
from functools import wraps
from questionPack import qBank
import random


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def mark(submission):
    '''a function that receives result from the front end and marks it '''
    score = 0
    correct = submission['correct']
    selected = submission['answers']
    for correctOption,selectedOption in zip(correct,selected):
        if correctOption == selectedOption:
            score+=1
    return score


def format_for_table(req):
    ''' helper function to format incoming form data to be suitable for db persistence. Takes the input and returns suitable data for the db'''
    topic = request.form['topic']
    question = request.form['question']
    option=request.form['options'].split(',')
    option = str(option)
    correct = request.form['correct']
    return topic,question,option,correct

def add_question_to_db(db_session,db,topic,question,option,correct):
    ''' helper function to add formated questions to db '''
    questions = db(topic,question,option,correct)     
    db_session.add(questions)
    db_session.commit()

def retrieve_questions_from_db(topic,db,limit):
    ''' retrieve the questions from the database '''
    result = db.query.filter_by(topic=topic).all()
    return random.sample(result,limit)


def format_questions_to_send (db_query_result,topic):
    '''helper function to format the questions retrieved from the database'''
    question_to_send = {
            "topic":topic,
            "status":200,
        }
    data=[]
    for results in db_query_result:
        # Remove the square brackets/comma from the string in options and store in a list. It is stored in the db as a string
        resultsList = results.options.replace(']','').replace('[','').split(',')
        data_structure = {
            "id_":results.id,
            "question":results.question,
            "answer":results.answer,
            'options':{
                'a':resultsList[0].replace("'",''),
                'b':resultsList[1].replace("'",''),
                'c':resultsList[2].replace("'",''),
                'd':resultsList[3].replace("'",''),
            }
        }

        data.append(data_structure)

    question_to_send['data'] = data
    return question_to_send
 
def percentagilize(score):
    '''convert the scores into a percentage'''
    quotient = score/45
    percentage = quotient * 100
    return percentage

def result_message(percentage):
    ''' A function to format the percentage score and pass to the frontend'''
    if percentage >= 70:
        return 'gold'
    elif percentage >= 50 and percentage <= 69:
        return 'silver'
    elif percentage > 30 and percentage <= 49:
        return 'bronze'
    else:
        return 'dust'
    
        