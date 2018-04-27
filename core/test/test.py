# Imports
import os
import json

# Constants
directory = os.path.realpath('.')

# Variables
with open(directory + '\\questions.json') as file:
    question_dict = json.load(file)
    questions = []
    for question_key in question_dict:
        questions.append(question_dict[question_key])

for q in questions:
    q = q.replace('?', '.')
    q = q.replace('!', '.')
    splited_question = q.split('.')
    for part in splited_question:
        if part is '':
            splited_question.remove(part)
    print(splited_question)
