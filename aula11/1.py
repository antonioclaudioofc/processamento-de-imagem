# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('carro.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5),np.uint)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
top_black_hat = cv2.morphologyEx(blackhat, cv2.MORPH_TOPHAT, kernel)


plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(tophat)
plt.title('TopHat')
plt.subplot(223), plt.imshow(blackhat)
plt.title('BlackHat')
plt.subplot(224), plt.imshow(top_black_hat)
plt.title('TopHat + BlackHat')

plt.tight_layout()
plt.show()