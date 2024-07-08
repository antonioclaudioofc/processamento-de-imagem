import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('logo.jpeg')

def ajuste_brilho(img,br):
    brilho=[br,br,br]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.minimum(img[y,x]+brilho,[255,255,255])
    return res

def ajuste_contraste(img,con):
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum(0, np.minimum(255, img[y, x] * con))
    return res

def ajuste_negativo(img):
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum(0, 255 - img[y, x])
    return res

cv2.namedWindow('Brilho')
brilho=0
result=imagem
con = 0.1

while(True):
    cv2.imshow('Brilho',result)
    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho=min(brilho+25,255)
        result=ajuste_brilho(imagem,brilho)
    elif k == ord('z'):
        brilho=max(brilho-25,0)
        result=ajuste_brilho(imagem,brilho)
    elif k == ord('s'):
        con += 0.1
        result=ajuste_contraste(imagem,con)
    elif k == ord('x'):
        con -= 0.1
        result=ajuste_contraste(imagem,con)
    elif k == ord('n'):
        result=ajuste_negativo(imagem)

cv2.destroyAllWindows()