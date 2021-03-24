import numpy as np  
import cv2


def maskFromImage(image, threshold):
    ret, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    mask = thresh < 200
    return mask.flatten(), thresh

img = cv2.imread('2d.png', 0)
_, i = maskFromImage(img, 0)

cv2.imshow('imagef', i)

cn, _ = cv2.findContours(i, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in cn:
    a = cv2.contourArea(c)
    print('area: ', a)
    p = cv2.arcLength(c,True)
    ci = p**2/(4*np.pi*a)
    x, y, w, h = cv2.boundingRect(c)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if ci > 1.2:
        #cv2.rectangle(i_c, (x, y), (x+w, y+h), 0,-1)
        i=cv2.putText(i,'R', (int(x+w/3), int(y+h/1.5)), font,.25,0,1)
    else:
        i=cv2.putText(i,'C', (int(x+w/3), int(y+h/1.5)), font,.25,0,1)
        # cv2.rectangle(i_r, (x, y), (x+w, y+h), 0,-1)

cv2.imshow('image', i)
cv2.waitKey(0)
cv2.destroyAllWindows()


