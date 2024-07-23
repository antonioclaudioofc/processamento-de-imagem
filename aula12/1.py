import cv2
import numpy as np

path_video = '../aula03/IFMA_caxias.mp4'

capture = cv2.VideoCapture(path_video)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True: 
            frame = cv2.Canny(frame,100,300)

            cv2.imshow('CAMPUS CAXIAS', frame)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()