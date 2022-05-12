from comparehist import CompareHist
import keyboard
import getarea
import mss
import numpy as np
import pydirectinput
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')
card = -1


def on_press(event):
    global card
    if event.event_type != 'down':
        return
    print("Key:", event.name, "Scan Code:", event.scan_code)


def on_red_press(event):
    global card
    if event.event_type != 'down':
        return
    pydirectinput.keyDown("w")
    pydirectinput.keyUp("w")
    card = 1
    return


def on_blue_press(event):
    global card
    if event.event_type != 'down':
        return
    pydirectinput.keyDown("w")
    pydirectinput.keyUp("w")
    card = 2
    return


def on_yellow_press(event):
    global card
    if event.event_type != 'down':
        return
    pydirectinput.keyDown("w")
    pydirectinput.keyUp("w")
    card = 3
    return


def main():
    global card
    ch = CompareHist()
    try:
        if config.getboolean('config', 'debug'):
            print('Debug mode is on, your keyboard and mouse input will be displayed below:')
            keyboard.hook(on_press, suppress=False)

        red_key = config.get('keybind', 'red')
        yellow_key = config.get('keybind', 'yellow')
        blue_key = config.get('keybind', 'blue')
    except Exception:
        print('Missing config.ini file!')
        exit(1)
        return

    if red_key == yellow_key or red_key == blue_key or yellow_key == blue_key:
        print(red_key, yellow_key, blue_key)
        print('Error: Two of keybinds are the same')
        exit(1)
    if "w" == red_key or "w" == yellow_key or "w" == blue_key:
        print('Error: w key is reserved for normal use')
        exit(1)

    while True:
        area = getarea.get_area()
        if area is not None:
            print("Abilities area found, start running...")
            break
        time.sleep(2)
    try:
        keyboard.hook_key(red_key, on_red_press, suppress=False)
        keyboard.hook_key(blue_key, on_blue_press, suppress=False)
        keyboard.hook_key(yellow_key, on_yellow_press, suppress=False)
    except ValueError:
        print('Error: Keybinds are not valid, please check config.ini')
        exit(1)

    with mss.mss() as sct:
        while True:
            image = np.array(sct.grab(area))
            if ch.cardCheck(image, card):
                pydirectinput.keyDown("w")
                pydirectinput.keyUp("w")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nProgram terminated')
