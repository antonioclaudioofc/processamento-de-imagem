import cv2
import numpy as np
img = cv2.imread('ifma.jpg')
img = cv2.resize(img, (600,600))

(row, col) = img.shape[0:2]

new_width = row // 3
new_height = col // 3

new_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

for i in range(0, row, 3):
    for j in range(0, col, 3):
        if i + 2 < row and j + 2 < col:
            block = img[i:i+3, j:j+3]

            central_pixel = block[1, 1]

            new_image[i//3, j//3] = central_pixel

cv2.imwrite("1.jpg", new_image)
cv2.imshow('Original', img)
cv2.imshow('Nova Imagem', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
