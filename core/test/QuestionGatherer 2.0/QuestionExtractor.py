import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import randint as r
import requests


# OCR
def send_ocr(filename, overlay=False, api_key='acf7c56e6088957', language='ger', pdf=False):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isCreateSearchablePdf': pdf
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()


# Settings
method = cv2.TM_CCOEFF_NORMED
f_name = 'C:\\Users\\vince\\Desktop\\63.jpg'

# Image
img_rgb = cv2.imread(f_name)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)


def find(template, color, img, threshold=0.85):
    print(color)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, method)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), color, 2)


# Numbers
find(cv2.imread("C:\\Users\\vince\\Desktop\\number.png", 0), (0, 0, 255), img_rgb, 0.7)
find(cv2.imread("C:\\Users\\vince\\Desktop\\number2.png", 0), (0, 0, 255), img_rgb, 0.7)

# Parts
res = send_ocr(filename=f_name, language='ger', overlay=True, pdf=True)
file = open("C:\\Users\\vince\\Desktop\\asd.npp", "w")
file.write(str(res))
file.close()

cv2.imwrite('C:\\Users\\vince\\Desktop\\res.png', img_rgb)
