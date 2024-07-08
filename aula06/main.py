import cv2
import numpy as np


RED = (0, 0, 255)

def draw_circle(event,x,y,flags,param):
    global pos_x
    global pos_y

    if event == cv2.EVENT_LBUTTONDOWN:
        pos_x = x 
        pos_y = y 
        cv2.circle(img,(x,y),3,RED,-1)

img = cv2.imread('ifma.jpg')

pos_x = 0
pos_y = 0
angle = 10
rows,cols = img.shape[:2]

cv2.namedWindow('Logo IF')
cv2.setMouseCallback('Logo IF',draw_circle)


while(1):
    cv2.imshow('Logo IF',img)

    if cv2.waitKey(20) & 0xFF == ord('r'):
        rot = cv2.getRotationMatrix2D((pos_x,pos_y),angle,1)
        img = cv2.warpAffine(img,rot,(cols,rows))

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()