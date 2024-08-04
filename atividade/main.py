import cv2
import numpy as np

path_video = '../aula03/IFMA_caxias.mp4'

capture = cv2.VideoCapture(path_video)

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))

img = cv2.imread('logo-if-vertical.png')

min_scale_percent = 25
max_scale_percent = 75
scale_percent = min_scale_percent
frame_count = 0
scale_change_rate = 1

if not capture.isOpened():
    print("Erro ao carregar o vídeo")
else:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            
            if frame_count >= 7:
                if scale_percent >= max_scale_percent:
                    scale_percent = min_scale_percent
                else:
                    scale_percent += scale_change_rate
                frame_count = 0

            img_height = int(frame_height * scale_percent / 100)
            aspect_ratio = img.shape[1] / img.shape[0]
            img_width = int(img_height * aspect_ratio)
            dim = (img_width, img_height)

            resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            gray = resized_img.copy()
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

          
            x_offset = (frame_width - img_width) // 2
            y_offset = (frame_height - img_height) // 2

            frame = cv2.GaussianBlur(frame, (25, 25), 2)

            _, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)


            roi = frame[y_offset:y_offset+img_height, x_offset:x_offset+img_width]

            frame_mask = cv2.bitwise_and(roi, roi, mask=mask)
            img_mask = cv2.bitwise_and(resized_img, resized_img, mask=mask_inv)

            dst = cv2.add(frame_mask, img_mask)

            frame[y_offset:y_offset+img_height, x_offset:x_offset+img_width] = dst
            
            cv2.imshow("IFMA Caxias", frame)
            frame_count += 1
            
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        else: break

capture.release()
cv2.destroyAllWindows()
