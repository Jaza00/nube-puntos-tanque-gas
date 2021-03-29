import config
from pointCloud import *
import numpy as np
from vedo import *

# cargamos la nube de puntos
pointcloud = load('nubePuntosTanque.ply')

# obtenemos coordendas xyz de la nube de puntos
xyz = pointcloud.points()
# quitamos puntos atipicos
xyz = xyz[xyz[:,2]<1200]
xyz[:,2] = -xyz[:,2]
#volvemos a contruir la nube de puntos
pointcloud = Points(xyz, r=3.0)

xyz = pointcloud.projectOnPlane(plane='x').points()
axesRuler = buildRulerAxes(pointcloud, units="mm", axisRotation=90.0)
# obtenemos las coordenadas del punto mínimo y máximo de la nube de puntos
coordPuntoMin = getCoordPuntoMin(xyz)
coordPuntoMax = getCoordPuntoMax(xyz)

# transformamos el mínimo y máximo punto a un punto para visualizar en la nube
pMin = Points([np.array(coordPuntoMin)], c="r", r=10)
pMax = Points([np.array(coordPuntoMax)], c="r", r=10)

# agregamos barra de colores en función de la altura del tanque
pointcloud.cmap('magma', np.abs(xyz[:,2]-np.max(xyz[:,2])))
pointcloud.addScalarBar(title="Altura en mm")

# visualizamos todos los componentes
show(pointcloud, pMin, pMax, axesRuler, bg='white')