import config
from pointCloud import *
import cv2

vertices = loadPointCloud('../data/nubePuntos/GasTankStraightDown.ply')
COLOR = 'magma'

# transformar nube de puntos a imagen
xyz = vertices.points()
image = xyz2image(xyz)

# encontrar la máscara en donde se encuentra el cilindro
mask, thresh, (centroX, centroY, radio) = maskFromImage(image, 2)

# visualizar resultado
cv2.imshow('image', image)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()