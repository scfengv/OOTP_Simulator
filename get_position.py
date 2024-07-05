import time
import pyautogui

def get_position():
    time.sleep(2)
    print(pyautogui.position())

get_position()
