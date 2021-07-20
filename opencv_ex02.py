import cv2 

# OpenCV 기본소스
cam = cv2.VideoCapture(0) #0번이 기본카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #카메라 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #카메라 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID라는 비디오 코덱으로 녹화하겠다는 것
is_record = False                        #녹화상태 

while True:
    ret, frame = cam.read() #video를 읽음

    if ret:
        cv2.imshow('Original Video', frame) #카메라 영상을 CAM이라는 이름으로 창에 출력

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면
            break           #while문 탈출
        elif key == ord('c'):
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지 캡처 완료')
        elif key == ord('r') and is_record == False: #r을 입력하고 최초 레코딩을 시작하면 
            is_record = True
            video = cv2.VideoWriter('./capture/record.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            print('녹화시작')

        elif key == ord('r') and is_record == True: #녹화중이면 종료
            is_record = False
            video.release()
            print('녹화종료')     

        if is_record == True: #현재화면 녹화
            video.write(frame)    

cam.release()
cv2.destroyAllWindows()