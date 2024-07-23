# coding=utf-8
import cv2
import numpy as np

kernel = np.ones((3,3),np.uint8)

img = cv2.imread('moedas.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY_INV)

closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

canny = cv2.Canny(closing, 100, 300)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow('Contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
