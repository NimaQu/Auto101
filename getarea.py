import numpy as np
import cv2
import imutils
import mss


def get_area():
    template = cv2.imread('img/default.png')  # template image

    with mss.mss() as sct:
        # area = {"top": 720, "left": 640, "width": 1280, "height": 720}
        area = {"top": 0, "left": 0, "width": 2560, "height": 1440}
        image_o = np.array(sct.grab(area))

    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    image = cv2.cvtColor(image_o, cv2.COLOR_BGR2GRAY)

    loc = False
    threshold = 0.9
    w, h = template.shape[::-1]
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        resized = imutils.resize(template, width=int(template.shape[1] * scale))
        w, h = resized.shape[::-1]
        res = cv2.matchTemplate(image, resized, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)
        if len(list(zip(*loc[::-1]))) > 0:
            break

    try:
        area = {"top": list(zip(*loc[::-1]))[0][1], "left": list(zip(*loc[::-1]))[0][0], "width": w, "height": h}
    except IndexError:
        print("No abilities area found, will check in next 2 seconds")
        return
    return area


def get_img(area):
    with mss.mss() as sct:
        if area is None:
            return
        image = np.array(sct.grab(area))
        return image


def main():
    with mss.mss() as sct:
        area = get_area()

        if area is None:
            return

        image = np.array(sct.grab(area))

        winname = "Image"
        cv2.namedWindow(winname)
        cv2.moveWindow(winname, 1400, 750)
        cv2.imshow(winname, image)
        cv2.waitKey()
        cv2.destroyAllWindows()
        print(area)


if __name__ == '__main__':
    main()
