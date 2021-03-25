"""Gas Tank Straight Downr"""

from pointCloud import *
from vedo import *
import numpy as np
import cv2

COLOR = 'magma'
vertices = load('Gas Tank Straight Down.ply')

xyz = vertices.points()
image = xyz2image(xyz)
mask, thresh, (x, y, r) = maskFromImage(image, 2)

xyz = xyz[mask == False]
xyz = xyz[xyz[:,2] < 1200]

xyz1 = xyz.copy() 
xyz1[:,0] = + xyz1[:,0] + 400

xyz2 = xyz1.copy() 
xyz2[:,0] = + xyz2[:,0] + 400

xyz3 = xyz.copy() 
xyz3[:,1] = + xyz[:,1] + 400

xyz4 = xyz1.copy() 
xyz4[:,1] = + xyz1[:,1] + 400

xyz5 = xyz2.copy() 
xyz5[:,1] = + xyz2[:,1] + 400

print('number of points: ', len(xyz))

#xyz = knNeighbors(xyz, 5)
vertices, scalars = xyz2pointCloud(xyz, COLOR, 1)
vertices1, _ = xyz2pointCloud(xyz1, COLOR, 1)
vertices2, _ = xyz2pointCloud(xyz2, COLOR, 1)
vertices3, _ = xyz2pointCloud(xyz3, COLOR, 1)
vertices4, _ = xyz2pointCloud(xyz4, COLOR, 1)
vertices5, _  = xyz2pointCloud(xyz5, COLOR, 1)

pic = Picture("logoIntecol.png")
pic.scale(3.0).rotateX(270)

show(vertices, vertices1,vertices2, vertices3, vertices4, vertices5, pic, __doc__, bg='k')
#show(rul,vertices,vig, vertices, vertices1,vertices2, vertices3, vertices4, vertices5, rul, __doc__, bg2='lb', viewup='y')


plt.plot(xyz[:,1]+600, -xyz[:,2]+1200, color='k')
plt.show()

