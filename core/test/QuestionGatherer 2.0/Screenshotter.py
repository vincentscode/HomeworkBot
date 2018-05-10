import pyautogui as pg
import ctypes
import numpy as np
import cv2
from time import sleep
from desktopmagic.screengrab_win32 import getScreenAsImage


def get_screen():
    screenshot = cv2.cvtColor(np.array(getScreenAsImage()), cv2.COLOR_RGB2BGR)
    screenshot = screenshot[167:(1080-45), 0:1920]
    return screenshot


# Zoom
def zoom():
    ctypes.windll.user32.SetCursorPos(-1140, 1055)
    pg.click()
    ctypes.windll.user32.SetCursorPos(-1140, 500)
    for i in range(8):
        pg.click()


# Upper-Left
def move_upper_left():
    ctypes.windll.user32.SetCursorPos(-40, 500)
    pg.mouseDown()
    ctypes.windll.user32.SetCursorPos(1920, 1080)
    pg.mouseUp()


# Down-Left
def move_down_left():
    ctypes.windll.user32.SetCursorPos(-1900, 800)
    pg.mouseDown()
    ctypes.windll.user32.SetCursorPos(1920, 40)
    pg.mouseUp()


# Down-Right
def move_down_right():
    ctypes.windll.user32.SetCursorPos(-40, 800)
    pg.mouseDown()
    ctypes.windll.user32.SetCursorPos(-1920, 800)
    pg.mouseUp()


# Upper-Right
def move_upper_right():
    ctypes.windll.user32.SetCursorPos(-40, 300)
    pg.mouseDown()
    ctypes.windll.user32.SetCursorPos(-40, 1080)
    pg.mouseUp()


wait_time_move = 1.7
wait_time_switch = 3

iter = 0
sleep(0)
while True:
    zoom()

    move_upper_left()
    sleep(wait_time_move)
    img1 = get_screen()

    move_down_left()
    sleep(wait_time_move)
    img2 = get_screen()

    move_down_right()
    sleep(wait_time_move)
    img3 = get_screen()

    move_upper_right()
    sleep(wait_time_move)
    img4 = get_screen()

    ctypes.windll.user32.SetCursorPos(-680, 1055)
    pg.click()
    height1, width1, channels = img1.shape
    height2, width2, _ = img2.shape
    height3, width3, _ = img3.shape
    height4, width4, _ = img4.shape

    full_image = np.ones((1506, 2199, channels), np.uint8)

    full_image[0:height1, 0:width1] = img1
    full_image[638:1506, 1:width2+1] = img2
    full_image[637:1505, 281:2199] = img3[0:height3, 1:(width3-1)]
    full_image[0:height4, (2199-width4):2199] = img4

    cv2.imwrite('C:\\users\\vince\\desktop\\book8\\{}.jpg'.format(iter), full_image)
    sleep(2.5)
    iter += 1