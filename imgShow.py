import cv2
import numpy as np

img = cv2.imread('box.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgGray = np.float32(imgGray)

corners = cv2.goodFeaturesToTrack(imgGray, 100, 0.01, 10)
corners = np.int0(corners)

for item in corners:
    x, y = item.ravel()
    cv2.circle(img, (x, y), 3, [0, 255, 0], -1)

cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyWindows()