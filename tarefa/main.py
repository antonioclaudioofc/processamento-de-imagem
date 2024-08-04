import cv2
import numpy as np

img = cv2.imread("cars.png")
img = cv2.resize(img, (692, 290))

mask = np.zeros(img.shape[:2], np.uint8)
cv2.circle(mask, (450, 129), 125, 255, -1)

mask_inv = cv2.bitwise_not(mask)

blur = cv2.GaussianBlur(img, (9, 9), 0)

img_part = cv2.bitwise_and(img, img, mask=mask)
blur_part = cv2.bitwise_and(blur, blur, mask=mask_inv)

res = cv2.add(img_part, blur_part)

cv2.imshow("Imagem", res)

cv2.waitKey(0)
cv2.destroyAllWindows()