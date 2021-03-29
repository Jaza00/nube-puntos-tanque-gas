import config
from pointCloud import *
import cv2

vertices = loadPointCloud('../data/nubePuntos/GasTankStraightDown.ply')

xyz = vertices.points()
image = xyz2image(xyz)

falseColorImage = getFalseColorImage(image, 'magma')
mask, thresh, (centroX, centroY, radio) = maskFromImage(image, 2)

cv2.line(falseColorImage, (centroX,centroY), (centroX + radio, centroY), (255,0,255), 2)
cv2.putText(falseColorImage,'Radio: %0.0fmm' % radio, (centroX, centroY+20), 1, 1, (0,0,0), 2)

cv2.imshow('image', image)
cv2.imshow('falseColorImage', falseColorImage)
cv2.waitKey(0)
cv2.destroyAllWindows()