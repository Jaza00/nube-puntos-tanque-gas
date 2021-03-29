import config

from pointCloud import *

import cv2

image = cv2.imread('../public/images/pointCloud2image.png', 0)

print(image)

circles = detectarCircunferencia(image)
print(circles)