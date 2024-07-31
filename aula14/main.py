import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.png")
box = cv2.imread("box.png")

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(box, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

matches = sorted(matches, key= lambda x:x.distance)

result = cv2.drawMatches(img, kp1, box, kp2,matches[:40], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(result)

plt.show()