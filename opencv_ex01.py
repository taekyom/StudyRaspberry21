import cv2 

# OpenCV 기본소스
cam = cv2.VideoCapture(0) #0번이 기본카메라
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #카메라 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #카메라 창 높이


while True:
    ret, frame = cam.read() #video를 읽음

    if ret:
        cv2.imshow('Original Video', frame) #카메라 영상을 CAM이라는 이름으로 창에 출력

        key = cv2.waitKey(1)
        if key == ord('q'): #q를 입력받으면
            break           #while문 탈출

cam.release()
cv2.destroyAllWindows()