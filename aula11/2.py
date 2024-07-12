# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('utechia.jpeg')
img = cv2.resize(img, (200,200))

kernel = np.ones((3,3),np.uint8)

kernel_1 = np.array([
 [1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
], dtype=np.uint8)

kernel_2 = np.array([
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
], dtype=np.uint8)

kernel_2_1 = np.array([
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0],
], dtype=np.uint8)

kernel_2_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(12,12))

example_1 = cv2.erode(img, kernel_1, iterations=3)

example_2 = cv2.erode(img, kernel_2, iterations=12)
example_2 = cv2.dilate(example_2, kernel_2_1, iterations=12)
example_2 = cv2.erode(example_2, kernel_2_2, iterations=2)

border = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
example_1 = cv2.addWeighted(example_1, 1, border, 1, 0)
# example_2 = cv2.addWeighted(example_2, 1, border, 1, 0)


plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(example_1)
plt.title('Exercicio 01')
plt.subplot(223), plt.imshow(example_2)
plt.title('Exercicio 02')

plt.tight_layout()
plt.show()