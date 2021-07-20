import cv2
import numpy as np

#카메라 기본 틀
##영상 자르기
cap = cv2.VideoCapture(0) #번호 0부터 시작, = cap.open(웹캠 오픈)

#높이, 넓이 수동설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#무한루프(q를 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, ret true/false
    h, w, c = frame.shape
    crop = frame[:, :int(w/2)]

    if ret != True: break #ret이 false면 루프 탈출

    cv2.imshow('RealTime CAM', frame) #로드한 영상을 창에 출력
    cv2.imshow('Cropped Result', crop)

    if cv2.waitKey(1) == ord('q'): #q를 입력하면 루프 탈출
        break

cap.release() # =cap.close(웹캠 해제)
cv2.destroyAllWindows() #메모리 해제    
