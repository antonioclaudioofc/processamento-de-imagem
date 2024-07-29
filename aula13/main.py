import cv2
import numpy as np

path_video = '../aula03/IFMA_caxias.mp4'
path_face_cascade = 'haarcascade/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(path_face_cascade)

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
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(frame_gray, minSize=(40, 40), scaleFactor=1.01)

            for (x,y,w,h) in faces:
                frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            cv2.imshow('CAMPUS CAXIAS', frame)
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            
        else: break

capture.release()
cv2.destroyAllWindows()