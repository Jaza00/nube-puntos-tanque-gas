"""Gas Tank Straight Downr"""

from pointCloud import *
from vedo import *
import numpy as np
import cv2

vertices = load('Gas Tank Straight Down.ply')
colorPoint = 'magma'

xyz = vertices.points()
image = xyz2image(xyz)

falseColorImage = getFalseColorImage(image, colorPoint)
mask, thresh, (x, y, r) = maskFromImage(image, 1)

cv2.line(falseColorImage, (x,y), (x + r, y), (255,0,255), 2)
cv2.putText(falseColorImage,'Radio: ' + str(r*0.1) + 'cm', (x, y+20), 1, 1, (0,0,0), 2)

xyz = xyz[mask == False]
xyz = xyz[xyz[:,2] < 1200]

xyz[:,2] = -xyz[:,2]
xyz[:,1] = -xyz[:,1]


vertices, scalars = xyz2pointCloud(xyz, colorPoint, 3.0)

xyz = vertices.projectOnPlane(plane='x').points()

pMin = np.where(xyz[:,2] == np.min(xyz[:,2]))[0]
xyz[pMin].tolist()
punto1 = tuple(xyz[pMin].tolist()[0])


pMax = np.where(xyz[:,2] == np.max(xyz[:,2]))[0]
xyz[pMax].tolist()
punto2 = tuple(xyz[pMax].tolist()[0])

# measure the angle formed by 3 points
vig = vertices.vignette('Radio cilindro: \n' + str(r) + 'mm')
vertices.cmap(colorPoint, -scalars+np.max(xyz[:,2]))

vertices.addScalarBar(title="Altura en mm")
rul = Ruler(punto1, punto2, prefix='Altura =', units='mm', lw=2, axisRotation=180.0)
ax3 = buildRulerAxes(vertices, units="mm", axisRotation=90.0)
pMin = Points(xyz[pMin], c="r", r=10)
pMax = Points(xyz[pMax], c="r", r=10)

pic = Picture("logoIntecol.png")

x, y, z = punto2
pic.scale(2.0).rotateZ(90).rotateY(90).pos((x-300, y+400, z))

show(vertices, ax3, pMax, __doc__, bg='white', viewup='z')
#show(rul,vertices,vig, ax3, pMin, pMax, pic, __doc__, bg='k9', viewup='z')

