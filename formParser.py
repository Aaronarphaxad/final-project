# Function to get form input and store in multiple variables
def formparser(request):
    topic = request.form['topic']
    questions = request.form['question']
    options = request.form['options'].split(',')
    correctAnwer = request.form['correct']
    return topic,questions,options,correctAnwer

# Function to add options of a question to a list containing questions at index 0, then other options in one list.
# Then selected answers in a list too 
def getInitialList(questions,options,correctAnswer,realOptions,answersList):
    realOptions.append(questions)
    for option in options:
        realOptions.append(option)
    answersList.append(correctAnswer)
    return answersList,realOptions
    
def getFinalList(realOptions,bigOptionList):      
    bigOptionList.append(realOptions)
    return bigOptionList