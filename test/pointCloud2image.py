import config
from pointCloud import *
import cv2

pointCloud = loadPointCloud('../data/nubePuntos/GasTankStraightDown.ply')
xyz = pointCloud.points()

# transformación de nube de puntos a imagen
image = xyz2image(xyz)

cv2.imshow('original image', image)
falseColorImage = getFalseColorImage(image, 'magma')
cv2.imshow('false color image', falseColorImage)
cv2.waitKey(0)
cv2.destroyAllWindows()