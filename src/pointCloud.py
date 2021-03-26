from vedo import *
import matplotlib.pyplot as plt 
import numpy as np
import cv2

def knNeighbors(vertices, nNeighbors):
    """ 
    knNeighbors: disminuye el ruido y agrupo los puntos con sus vecionos más cercanos
    parameters: vertices y el número de vecinos a tener en cuenta
    return: nueva nube de puntos
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
    scalars = -xyz[:, 2] / 2.5
    image = scalars.reshape(-1, 640, )
    image = image.astype(np.uint8)
    cv2.imwrite('xyz2image.png', image)
    return image

def maskFromImage(image, radio):
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
    print('color: ', nameColor)
    if nameColor == 'rainbow':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_RAINBOW)
    if nameColor == 'jet':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_JET)
    if nameColor == 'hsv':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_HSV)
    if nameColor == 'magma':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_MAGMA)
    if nameColor == 'rainbow-inv':
        newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_RAINBOW)
        newImage = abs(255 - newImage)
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

def xyz2pointCloud(xyz, colorPoint, radio):
    vertices = Points(xyz, r=radio)
    # agrega el falso color jet
    scalars = vertices.points()[:, 2]
    vertices.pointColors(-scalars, cmap=colorPoint)
    return vertices, scalars

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