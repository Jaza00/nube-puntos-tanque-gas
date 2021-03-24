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
    cv2.imwrite('2d.png', image)
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

def xyz2pointCloud(xyz, colorPoint):
    vertices = Points(xyz, r=1.0)
    # agrega el falso color jet
    scalars = vertices.points()[:, 2]
    vertices.pointColors(-scalars, cmap=colorPoint)
    return vertices


vertices = load('Gas Tank Straight Down.ply')
verticesTankOfset = load('Gas Tank Offset.ply')
#vertices = load('Bucket half full of clear water.ply')
#vertices = load('Bucket half full of cloudy water.ply')
#vertices = load('Empty Bucket.ply')
colorPoint = 'viridis'

xyz = vertices.points()
image = xyz2image(xyz)

falseColorImage = getFalseColorImage(image, colorPoint)
mask, thresh, (x, y, r) = maskFromImage(image, 2)

cv2.line(falseColorImage, (x,y), (x + r, y), (255,0,255), 2)
cv2.putText(falseColorImage,'Radio: ' + str(r*0.1) + 'cm', (x, y+20), 1, 1, (0,0,0), 2)

cv2.imshow('image', image)
cv2.imshow('falseColorImage', falseColorImage)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

xyz = xyz[mask == False]
xyz = xyz[xyz[:,2] < 1200]


copiaXyz1 = xyz.copy() 
copiaXyz1[:,0] = + copiaXyz1[:,0] + 400
copiaXyz2 = copiaXyz1.copy() 
copiaXyz2[:,0] = + copiaXyz2[:,0] + 400
copiaXyz3 = xyz.copy() 
copiaXyz3[:,1] = + xyz[:,1] + 400
copiaXyz4 = copiaXyz1.copy() 
copiaXyz4[:,1] = + copiaXyz1[:,1] + 400
copiaXyz5 = copiaXyz2.copy() 
copiaXyz5[:,1] = + copiaXyz2[:,1] + 400


scalar = np.array([[1.5, 0.0, 0.0],
                   [0.0, 1.5, 0.0],
                   [0.0, 0.0, 1.5]])

nuevaCopia = np.dot(scalar, copiaXyz5.T).T
print('number of points: ', len(xyz))

xyzTankOffset = verticesTankOfset.points()
xyzTankOffset = xyzTankOffset[xyzTankOffset[:,2] < 1200]

#xyz = knNeighbors(xyz, 5)
vertices = xyz2pointCloud(xyz, colorPoint)
copiaVertices1 = xyz2pointCloud(copiaXyz1, colorPoint)
copiaVertices2 = xyz2pointCloud(copiaXyz2, colorPoint)
copiaVertices3 = xyz2pointCloud(copiaXyz3, colorPoint)
copiaVertices4 = xyz2pointCloud(copiaXyz4, colorPoint)
copiaVertices5 = xyz2pointCloud(nuevaCopia, colorPoint)
verticesTank = xyz2pointCloud(xyzTankOffset, colorPoint)
show(vertices, copiaVertices1,copiaVertices2, copiaVertices3, copiaVertices4, copiaVertices5, bg='k', viewup='y')

plt.plot(xyz[:,1]+600, -xyz[:,2]+1200, color='k')
plt.show()

