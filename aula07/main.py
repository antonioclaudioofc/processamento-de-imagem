import cv2
import numpy as np

path_img = '../aula04/ifma.jpg'
path_logo = '../aula05/logo.jpg'

img = cv2.imread(path_img)

logo = cv2.imread(path_logo) 
logo = cv2.resize(logo, (400, 150), interpolation=cv2.INTER_AREA) 

(row, col) = logo.shape[0:2]

roi = img[0:row, 0:col]

logogray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)    
ret, mask_inv = cv2.threshold(logogray, 200, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
logo_fg = cv2.bitwise_and(logo,logo,mask = mask)

dst = cv2.add(img_bg,logo_fg)

img[0:row, 0:col ] = dst

cv2.imshow('Resultado',img)

cv2.waitKey(0)
cv2.destroyAllWindows()