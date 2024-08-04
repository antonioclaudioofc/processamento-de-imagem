import cv2

path_img = "../aula05/logo.jpg"

img = cv2.imread("ifma.jpg")
logo = cv2.imread(path_img)

logo = cv2.resize(logo, (200, 100), interpolation=cv2.INTER_AREA)

(row, col) = logo.shape[0:2]
roi = img[0:row, 0:col]

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(logo_gray, 254, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(roi, roi, mask=mask)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask_inv)

dst = cv2.add(img_bg, logo_fg)

img[0:row, 0:col] = dst

telea = cv2.inpaint(dst, mask_inv, 3, cv2.INPAINT_TELEA)

img[0:row, 0:col] = telea

cv2.imshow("Imagem", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
