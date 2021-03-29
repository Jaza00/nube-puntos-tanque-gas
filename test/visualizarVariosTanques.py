"""Gas Tank Straight Downr"""

import config
from pointCloud import *
import numpy as np

# cargar nube de puntos .ply
pointCloud = loadPointCloud('../data/nubePuntos/GasTankStraightDown.ply')

# obtener coordenadas de los puntos
xyz = pointCloud.points()

# obtener imagen de profundidad     
image = xyz2image(xyz)

# segementar el tanque de gas
mask, thresh, _ = maskFromImage(image, 2)
xyz = xyz[mask == False]

# hacer varios copias y desplazamientos sobre la nube de puntos principal
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

# fusionamos todas las coordenadas
xyz = np.insert(xyz, xyz.shape[0], xyz1, 0)
xyz = np.insert(xyz, xyz.shape[0], xyz2, 0)
xyz = np.insert(xyz, xyz.shape[0], xyz3, 0)
xyz = np.insert(xyz, xyz.shape[0], xyz4, 0)
xyz = np.insert(xyz, xyz.shape[0], xyz5, 0)

# transformas las coordenadas a nube de puntos
pointCloud = xyz2pointCloud(xyz)


showPointCloud([pointCloud], 5000, 'turbo', 1.0, bg='k')




