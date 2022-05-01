from __future__ import print_function
from __future__ import division
import cv2 as cv


class CompareHist:
    def __init__(self):
        blue = cv.imread('img/blue.png')
        yellow = cv.imread('img/yellow.png')
        red = cv.imread('img/red.png')

        if blue is None or yellow is None or red is None:
            print('Could not open or find the images!')
            exit(0)

        hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
        hsv_yellow = cv.cvtColor(yellow, cv.COLOR_BGR2HSV)
        hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)

        ## [Using 50 bins for hue and 60 for saturation]
        h_bins = 50
        s_bins = 60
        self.histSize = [h_bins, s_bins]

        # hue varies from 0 to 179, saturation from 0 to 255
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        self.ranges = h_ranges + s_ranges  # concat lists

        # Use the 0-th and 1-st channels
        self.channels = [0, 1]
        ## [Using 50 bins for hue and 60 for saturation]

        self.hist_red = cv.calcHist([hsv_red], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(self.hist_red, self.hist_red, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        self.hist_blue = cv.calcHist([hsv_blue], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(self.hist_blue, self.hist_blue, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        self.hist_yellow = cv.calcHist([hsv_yellow], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(self.hist_yellow, self.hist_yellow, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    def mainn(self, target_img):
        src_test1 = target_img

        if src_test1 is None:
            return

        ## [Convert to HSV]
        hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)

        ## [Convert to HSV half]

        ## [Calculate the histograms for the HSV images]

        hist_target = cv.calcHist([hsv_test1], self.channels, None, self.histSize, self.ranges, accumulate=False)
        cv.normalize(hist_target, hist_target, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        ## [Apply the histogram comparison methods]

        red_test1 = cv.compareHist(self.hist_red, hist_target, cv.HISTCMP_CORREL)
        blue_test1 = cv.compareHist(self.hist_blue, hist_target, cv.HISTCMP_CORREL)
        yellow_test1 = cv.compareHist(self.hist_yellow, hist_target, cv.HISTCMP_CORREL)

        # print('Hist.Correlation.(base&screen): red_test1:', red_test1)
        # print('Hist.Correlation.(base&screen): blue_test1:', blue_test1)
        # print('Hist.Correlation.(base&screen): yellow_test1:', yellow_test1)

        if red_test1 > 0.9:
            return 'red'
        elif blue_test1 > 0.9:
            return 'blue'
        elif yellow_test1 > 0.9:
            return 'yellow'
        else:
            return None


if __name__ == '__main__':
    comparehist = CompareHist()
    comparehist.mainn()

