from flask import redirect, render_template, request, session
from functools import wraps
from questionPack import qBank


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


def mark(results):
    score = 0
    for result in results:
        if result[1] == '1':
            score += 1
        return score
    # for k,v in results.items():
    #     if v == '1':
    #         score += 1
    # return score
def format_for_table(req):
    ''' helper function to format incoming form data to be suitable for db persistence '''
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

def retrieve_questions_from_db(topic,db):
    ''' retrieve the questions from the database '''
    result = db.query.filter_by(topic=topic).all()
    return result


def format_questions_to_send (db_query_result,topic):
    '''helper function to format the questions retrieved from the database'''
    question_to_send = {
            "topic":topic,
            "status":200,
        }
    data=[]
    for results in db_query_result:
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

