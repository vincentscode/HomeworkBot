import cv2
import numpy as np
import os

template_dir = "C:\\Users\\vince\\Desktop\\patterns\\"
templates = []
for file in os.listdir(template_dir):
    f = cv2.imread(template_dir + file)
    templates.append(f)


def scan(img, template):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        sub = img[pt[1] + 15:pt[1] + h - 2, pt[0] + 15:pt[0] + w - 2]
        cv2.imwrite('C:\\Users\\vince\\Desktop\\out.png', sub)


if __name__ == '__main__':
    scan(cv2.imread('C:\\Users\\vince\\Desktop\\book5_cut\\1.png'), templates[len(templates)-1])
