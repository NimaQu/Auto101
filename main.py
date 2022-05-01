from comparehist import CompareHist
import getarea
import mss
import numpy as np
import pydirectinput
import time


def main():
    ch = CompareHist()
    while True:
        area = getarea.get_area()
        if area is not None:
            print("Abilities area found")
            break
        time.sleep(1)

    with mss.mss() as sct:
        while True:
            image = np.array(sct.grab(area))
            result = ch.mainn(image)
            if result is not None:
                if result == "yellow":
                    pydirectinput.keyDown("w")
                    pydirectinput.keyUp("w")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nProgram terminated')
