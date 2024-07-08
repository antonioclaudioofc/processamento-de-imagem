import cv2
import numpy as np
import random

capture = cv2.VideoCapture("video.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
prob = 0.03


def noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

if not capture.isOpened():
    print("Erro ao acessar camera ou abrir o vídeo")
else:
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:

            new_noise = noise(frame,prob)

            cv2.imshow('Input', new_noise)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                prob += 0.03
                print(f"Probabilidade de ruído: {prob:.2f}")

        else: 
            break

capture.release()
cv2.destroyAllWindows()