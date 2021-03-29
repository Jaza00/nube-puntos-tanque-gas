import  config
from pointCloud import *

pointCLoud = loadPointCloud(
        '../data/nubePuntos/GasTankStraightDown.ply')
        
showPointCloud([pointCLoud], 1200, 'magma', 1.0)