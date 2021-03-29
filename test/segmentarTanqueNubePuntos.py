import config
from  pointCloud import  *


pointCloud = loadPointCloud('../data/nubePuntos/GasTankStraightDown.ply')

# obtenemos las coordenadas de cada punto de la nube
xyz = pointCloud.points()

# transformamos nube de puntos a imagen 2D
image = xyz2image(xyz)

# encontramos la máscara de segmentación del circulo 
mask, tresh, (centroX, centroY, radio) = maskFromImage(image, 5)

# aplicamos la máscara sobre la nube de puntos 3D
xyzFondo = xyz[mask]

# transformamos las coordenadas xyz a nube de puntos
pointCloudFondo = xyz2pointCloud(xyzFondo)

# aplicamos la máscara sobre la nube de puntos 3D
xyzTanque = xyz[mask == False]

# transformamos las coordenadas xyz a nube de puntos
pointCloudTanque = xyz2pointCloud(xyzTanque)

# guardamos nube de puntos del tanque de gas
savePointCloud(pointCloudTanque, 'nubePuntosTanque.ply')

# visualizamos
showPointCloud([pointCloudFondo, pointCloudTanque], 1200, 'magma', 1.0)