# willow cutting script lvl 30-99
# south of port sarim


import pyautogui
import time


def logout():
    if pyautogui.locateCenterOnScreen('logout.png', confidence=0.9):
        pyautogui.moveTo(x=0, y=0)
    else:
        loop()


def countdown_timer():
    # Countdown timer
    print("Starting Script", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        time.sleep(1)
    print("Script Running")


def start_click():
    if pyautogui.locateOnScreen('runescape_willow_1.png', confidence=0.9):
        pyautogui.click(x=1017, y=479)
    else:
        print('no Match')
        pyautogui.moveTo(x=0, y=0)


def first_tree_complete():
    if pyautogui.locateOnScreen('stump_1.png', confidence=0.9):
        time.sleep(3)
        pyautogui.click(x=596, y=554)

    elif pyautogui.locateOnScreen('inventory_full_tree_1.png', confidence=0.9):
        fletching()

    else:
        first_tree_complete()


def second_tree_complete():
    if pyautogui.locateOnScreen('stump_2.png', confidence=0.9):
        time.sleep(3)
        pyautogui.click(x=1295, y=388)

    elif pyautogui.locateOnScreen('inventory_full_tree_2.png', confidence=0.9):
        fletching()

    else:
        second_tree_complete()


def fletching():
    pyautogui.click(x=1763, y=588)
    time.sleep(1)
    pyautogui.click(x=886, y=549)
    time.sleep(1)
    pyautogui.click(x=1079, y=706)
    time.sleep(50)
    if pyautogui.locateOnScreen('runescape_willow_1.png', confidence=0.9):
        pyautogui.click(x=1017, y=479)
        first_tree_complete()

    elif pyautogui.locateOnScreen('runescape_willow_2.png', confidence=0.9):
        pyautogui.click(x=891, y=550)
        second_tree_complete()

    else:
        pyautogui.moveTo(x=0, y=0)


def loop():
    first_tree_complete()
    second_tree_complete()
    logout()


countdown_timer()

start_click()
loop()
