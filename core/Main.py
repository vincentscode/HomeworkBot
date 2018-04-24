import sys
import os
import time

from Question import Question
from Interpreter import Interpreter
from Answerer import Answerer

if __name__ == '__main__':
    interpreter = Interpreter()
    answerer = Answerer()
    while True:
        print("Enter your question.")
        usr_in = input()
        q = Question(usr_in)
