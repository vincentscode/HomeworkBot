import pyautogui as pg
import ctypes
import numpy as np
import cv2
from time import sleep
from desktopmagic.screengrab_win32 import getScreenAsImage

iter = 0

ctypes.windll.user32.SetCursorPos(-680, 1055)

while True:
    screenshot = cv2.cvtColor(np.array(getScreenAsImage()), cv2.COLOR_RGB2BGR)
    pg.click()
    screenshot = screenshot[170:1030, 20:1900]
    cv2.imwrite('C:\\users\\vince\\desktop\\book5\\{}.png'.format(iter), screenshot)
    sleep(2.3)
    iter += 1