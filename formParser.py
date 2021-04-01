def formparser(request):
    topic = request.form['topic']
    questions = request.form['question']
    options = request.form['options'].split(',')
    correctAnwer = request.form['correct']
    return topic,questions,options,correctAnwer


def getInitialList(questions,options,correctAnwer,realOptions,answersList):
    realOptions.append(questions)
    for option in options:
        realOptions.append(option)
    answersList.append(correctAnwer)
    return answersList,realOptions
    
def getFinalList(realOptions,bigOptionList):      
    bigOptionList.append(realOptions)
    return bigOptionList