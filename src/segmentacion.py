import  cv2
import numpy as np

img = cv2.imread('2d.png')
imgCopy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        circle = cv2.circle(imgCopy, (x, y), r, (0, 255, 0), 4)
        mask = np.zeros(img.shape[:2], dtype="uint8")
        cv2.circle(mask, (x, y), r+20, 255, -1)
        masked = cv2.bitwise_and(img, img, mask=mask)
        ret, thresh = cv2.threshold(masked, 0, 255, cv2.THRESH_BINARY)
        mask = thresh < 200
	    #cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
# show the img image
cv2.imshow("masked", masked)
cv2.imshow("thresh", thresh)
cv2.imshow("img", img)
cv2.imshow("imgCopy", imgCopy)
cv2.waitKey(0)


cv2.destroyAllWindows()