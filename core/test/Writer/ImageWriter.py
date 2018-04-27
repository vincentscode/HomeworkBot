import os
from random import randint
import cv2
import numpy as np

current_dir = os.path.realpath('.')


def char2img(c):
    letters_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    letters_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['-', '!', '#', '$', '%', '&', '(', ')', ',', ';', '@', '~', '€', '+', '=', '.', ':', '>', '?', '\'', '/',
               '<', '*']
    special_dict = {'.': 'dot', ':': 'double_dot', '>': 'greater', '?': 'question_mark', '\'': 'quotes',
                    '/': 'slash', '<': 'smaller', '*': 'star'}
    
    small_dir = current_dir + '\\labeled\\letters_small\\'
    big_dir = current_dir + '\\labeled\\letters_big\\'
    digits_dir = current_dir + '\\labeled\\digits\\'
    special_dir = current_dir + '\\labeled\\special\\'

    filepath = ''

    if c in letters_small:
        filepath += small_dir
        filepath += c
    elif c in letters_big:
        filepath += big_dir
        filepath += c
    elif c in digits:
        filepath += digits_dir
        filepath += c
    elif c in special:
        filepath += special_dir
        if c in special_dict:
            filepath += special_dict[c]
        else:
            filepath += c
    else:
        print('Letter not recognized.')
        return ''

    files = os.listdir(filepath)
    rand = randint(0, len(files)-1)
    filepath += '\\' + files[rand]
    img = cv2.imread(filepath)
    return img


def string2img(s):
    char_width = 60
    ret = np.ones((119, char_width*len(s), 3), np.uint8)
    ret[:] = (255, 255, 255)
    i = 0
    for c in s:
        x = char2img(c)
        if x is not '':
            ret[0:119, i * char_width:i * char_width + char_width] = x[0:119, 30:90]
        i += 1

    return ret


cv2.imshow('win', string2img('hallo welt, wie gehts so? mir ist langweilig..'))
cv2.waitKey(0)