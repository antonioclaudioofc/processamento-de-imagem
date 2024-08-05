# coding=utf-8
import cv2
import numpy as np

kernel = np.ones((3,3),np.uint8)

img = cv2.imread('moedas.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_ ,mask = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

closing = cv2.morphologyEx(mask_inv, cv2.MORPH_CLOSE, kernel)

canny = cv2.Canny(mask_inv, 100, 300)

contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, 127, 2)

for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img, center, radius, (0, 255, 0), 2)
    cv2.putText(img, f'R: {radius}', (center[0] - 10, center[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)


cv2.imshow('Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
