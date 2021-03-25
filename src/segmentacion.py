"""Gas Tank Straight Downr"""

from pointCloud import *
from vedo import *
import numpy as np
import cv2

COLOR = 'magma'
vertices = load('Gas Tank Straight Down.ply')

xyz = vertices.points()
image = xyz2image(xyz)

falseColorImage = getFalseColorImage(image, COLOR)
mask, thresh, (x, y, r) = maskFromImage(image, 2)

cv2.line(falseColorImage, (x,y), (x + r, y), (255,0,255), 2)
cv2.putText(falseColorImage,'Radio: ' + str(r*0.1) + 'cm', (x, y+20), 1, 1, (0,0,0), 2)

cv2.imshow('image', image)
cv2.imshow('falseColorImage', falseColorImage)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)