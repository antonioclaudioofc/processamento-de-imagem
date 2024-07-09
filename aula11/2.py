# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('utechia.jpeg')

kernel = np.ones((23,23),np.uint)
kernel_1 = np.array([[1, 1, 1],
                   [1,  1, 1],
                   [1, 1, 1]])

erosion = cv2.erode(img,kernel,iterations = 1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

personzalized = cv2.filter2D(img, -1, kernel_1)

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(erosion)
plt.title('Erosão')
plt.subplot(223), plt.imshow(personzalized)
plt.title('Personzalizadas')


plt.tight_layout()
plt.show()