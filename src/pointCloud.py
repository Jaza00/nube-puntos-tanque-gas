from vedo import *
import numpy as np
import cv2


def loadPointCloud(path):
    """
    Carga una nube de puntos con extensión .ply, obt, etc.

    parameters: 
        path: string
            ruta del directorio donde se encuentra la nube de puntos

    return:
        pointCloud: nube de puntos de vedo
            nube de puntos con las propiedades de la librería vedo
    """

    pointCloud = load(path)
    return pointCloud

def showPointCloud(pointClouds, depth, colorPoint, rPoint, bg=None,):
    """
    Visualizar una nube de puntos

    parameters: 
        pointClouds: list
            lista de todas las nubes de puntos que se quiere visualizar

        depth: int
            máxima profundidad (eje z) permitido en la nube de puntos
        
        colorPoint: string
            nombre del falso color que se asignará a la nube de puntos
            posibles colores: viridis, magma, hot, winter, hsv, inferno, plasma, turbo, etc
        
        rPoint: int
            tamaño de los puntos de la nube de puntos

        bg: string
            color del fondo del espacio de visualización, por defecto es 'white'
    """

    plt = Plotter(shape=(1,len(pointClouds)))
    i = 0
    for pointCloud in pointClouds:
        xyz = pointCloud.points()
        xyz = xyz[xyz[:,2] < depth]
        pointCloud = Points(xyz, r=rPoint)
        scalars = pointCloud.points()[:, 2]
        pointCloud.pointColors(-scalars, cmap=colorPoint)
        if bg is not None:
            plt.show(pointCloud, at=i, bg=bg, viewup='z')
        else:
            plt.show(pointCloud, at=i, bg='white', viewup='z')
        i = i + 1
    plt.show(interactive=True)

def knNeighbors(vertices, nNeighbors):
    """ 
    Disminuye el ruido y agrupo los puntos con sus vecinos más cercanos

    parameters: 
        vertices: np.array
            array de las coordenadas de la nube de puntos
        
        nNeighbors: int
            número de vecinos a tener en cuenta en el filtro

    return:
        newPointCloud: np.array
            nueva nube de puntos
    """

    vertices = Points(vertices)
    newPointCloud = []
    
    for i in range(vertices.N()):
        pt = vertices.points()[i]
        ids = vertices.closestPoint(pt, N = nNeighbors, returnPointId=True)
        newPointCloud.append(
            np.mean(vertices.points()[ids], axis=0).tolist())
    newPointCloud = np.array(newPointCloud)

    return newPointCloud

def xyz2image(xyz):
    """
    transforma una nube de puntos a una imagen 2D

    parameters:
        xyz: np.array
        array de las coordenadas de los puntos de la nube de puntos

    return:
        image: np.array uint8
        imagen resultante de la nube de puntos
    """

    scalars = -xyz[:, 2] / 2.5
    image = scalars.reshape(-1, 640, )
    image = image.astype(np.uint8)
    cv2.imwrite('xyz2image.png', image)
    return image

def detectarCircunferencia(image):
    """
    Detecta una circunferencia en una imagen en escala de grises

    parameters:
        image: np.array
            imagen en escala de grises en la que se quiere detectar un círculo

    return:
        circulos: lista de tuplas
            lista en la que retorna todos los centros y radios de los círculos detectados
    """

    circulos = []
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.2, 90)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (centroX, centroY, radio) in circles:
            circulos.append((centroX, centroY, radio))
    return circulos

def maskFromImage(image, radio):
    """
    Encuentra la máscara de la imagen que corresponde a la circunferencia del tanque de gas

    parameters:
        image: np.array
            imagen en escala de grises

        radio: int
            radio adicional al radio de la circunferencia para conservar datos cercanos al tanque

    return:
        mask: np.array
            array de tamaño ancho*alto que corresponde a la máscara resultante 

        thresh: np.array
            array, imagen que visualiza la segmentación del tanque

        (x, y, r): tuple
            tupla que contiene el centro y radio de la circunferencia detectada
    """

    mask = None
    thresh = None
    imgCopy = image.copy()
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.2, 90)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            circle = cv2.circle(imgCopy, (x, y), r, (0, 255, 0), 4)
            mask = np.zeros(image.shape[:2], dtype="uint8")
            cv2.circle(mask, (x, y), r+radio, 255, -1)
            masked = cv2.bitwise_and(image, image, mask=mask)
            ret, thresh = cv2.threshold(masked, 0, 255, cv2.THRESH_BINARY)
            mask = thresh < 200
    return mask.flatten(), thresh, (x, y, r)

def getFalseColorImage( grayImage, nameColor):
    """
    Aplicar un falso color a una imagen en escala de grises

    parameters: 
        grayImage: np.array
            imagen en escala de grises

        nameColor: string
            nombre del falso color que se asignará a la nube de puntos
            posibles colores: viridis, magma, hot, winter, hsv, inferno, plasma, turbo, etc

    returns:
        newImage: np.array
            imagen con el falso color aplicado
    """

    newImage = None
    print('color: ', nameColor)
    if nameColor == 'rainbow':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_RAINBOW)
    if nameColor == 'jet':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_JET)
    if nameColor == 'hsv':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_HSV)
    if nameColor == 'magma':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_MAGMA)
    if nameColor == 'winter':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_WINTER)
    if nameColor == 'summer':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_SUMMER)
    if nameColor == 'cool':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_COOL)
    if nameColor == 'pink':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_PINK)
    if nameColor == 'hot':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_HOT)
    if nameColor == 'inferno':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_INFERNO)
    if nameColor == 'plasma':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_PLASMA)
    if nameColor == 'viridis':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_VIRIDIS)
    if nameColor == 'turbo':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_TURBO)
    if nameColor == '':
        newImage = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2RGB)
    return newImage

def xyz2pointCloud(xyz):
    """
    Transforma coordenadas xyz a una nube de puntos de vedo

    parameters:
        xyz: np.array
            array de las coordenadas de la nube de puntos

    return:
        pointCloud: pointCloud de vedo
            nube de puntos con las propiedades de la librería vedo
    """

    pointCloud = Points(xyz)
    return pointCloud

def savePointCloud(pointCloud, path):
    """
    Guardar nube de puntos en el equipo

    paramters:
        pointCloud: point cloud de vedo
            nube de puntos de la librería vedo
        
        path: string
            ruta en donde se quiere guardar la nube de puntos, el nombre debe tener extensión .ply
    """

    write(pointCloud,path)
    print('point cloud saved')

def getCoordPuntoMin(xyz):
    """
    Obtener la coordenada en donde se encuentra el mínimo valor de profundidad

    paramters:
        xyz: np.array
            array de las coordenadas de la nube de puntos
    
    return:
        coordPuntoMin: tuple
            tupla de la coordenada xyz del mínimo valor de profundidad
    """

    # obtenemos el índice del mínimo punto de la nube
    indexPuntoMin = np.where(xyz[:,2] == np.min(xyz[:,2]))[0]
    # obtenemos las coordenadas del mínimo punto
    xyz[indexPuntoMin].tolist()
    coordPuntoMin = tuple(xyz[indexPuntoMin].tolist()[0])
    return coordPuntoMin

def getCoordPuntoMax(xyz):
    """
    Obtener la coordenada en donde se encuentra el máximo valor de profundidad

    paramters:
        xyz: np.array
            array de las coordenadas de la nube de puntos
    
    return:
        coordPuntoMax: tuple
            tupla de la coordenada xyz del máximo valor de profundidad
    """  

    # obtenemos el índice del máximo punto de la nube
    indexPuntoMax = np.where(xyz[:,2] == np.max(xyz[:,2]))[0]
    # obtenemos las coordenadas del máximo punto
    xyz[indexPuntoMax].tolist()
    coordPuntoMax = tuple(xyz[indexPuntoMax].tolist()[0])
    return coordPuntoMax

def toMesh(coords):
    print("point cloud to mesh")
    d0 = Points(coords, r=2, c="b").legend("source")
    d1 = delaunay2D(coords, mode='fit')
    d1.color("r").wireframe(True).legend("delaunay mesh")
    cents = d1.cellCenters()
    ap = Points(cents).legend("cell centers")
    # NB: d0 and d1 are slightly different
    show(d0, d1, __doc__, at=0)
    show(d1, ap, at=1, interactive=1)


def toSurface(pts):
    print("point cloud to surface")
    s1 = Points(pts, r=2, c="b").clean(tol=0.005)
    coords = s1.points()
    mesh = delaunay2D(coords, mode='fit')
    mesh.color("r").wireframe(True).legend("delaunay mesh")
    vp = Plotter(N=3, axes=0)
    vp.show(mesh, at=0)
    pts = s1.clone()
    #pts = s1.clone().smoothMLS2D(f=0.8)  # smooth cloud
    print("Nr of points before cleaning nr. points:", pts.N())
    # impose a min distance among mesh points
    pts.clean(tol=0.005).legend("smooth cloud")
    print("             after  cleaning nr. points:", pts.N())
    vp.show(pts, at=1)
    # reconstructed surface from point cloud
    reco = recoSurface(pts, dims=300, radius=15).legend("surf. reco")
    print('show reco')
    vp.show(reco, at=2, axes=7, zoom=1.2, interactive=1)