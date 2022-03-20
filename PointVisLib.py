'''
library to aid with the display of points of the fingers and rotations in an easy to understand form
'''

import cv2 as cv
import numpy as np

width : int = 1920
height : int = 1080

blank = np.zeros((height,width), np.uint8)
blank = cv.resize(blank, (width, height))
print(blank)
cv.imshow("", blank)
cv.waitKey(1)
