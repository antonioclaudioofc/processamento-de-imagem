import cv2
import numpy as np

path_video = '../aula04/video.mp4'
path_logo = 'opencv.png'

logo = cv2.imread(path_logo) 
logo = cv2.resize(logo, (200, 225), interpolation=cv2.INTER_AREA) 

(row, col) = logo.shape[0:2]

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
            roi = frame[0:row, 0:col]

            logogray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
            ret, mask_inv = cv2.threshold(logogray, 200, 255, cv2.THRESH_BINARY)
            mask = cv2.bitwise_not(mask_inv)

            frame_now = cv2.bitwise_and(roi,roi)
            logo_fg = cv2.bitwise_and(logo,logo,mask = mask)

            dst = cv2.add(frame_now,logo_fg)

            frame[0:row, 0:col ] = dst
           
            cv2.imshow('CAMPUS CAXIAS', frame)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()