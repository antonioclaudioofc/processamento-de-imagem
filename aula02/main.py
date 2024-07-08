import cv2
img = cv2.imread('color_red.jpg')
img = cv2.resize(img, (350,505))

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

gray = img.copy()

(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		if(hsv[i,j][0]<170) or (hsv[i,j][0]>200):
			gray[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Original', img)
cv2.imshow('HSV', hsv)
cv2.imshow('Result', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
