import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

#카메라 기본 틀
##영상에 글자 출력
cap = cv2.VideoCapture(0) #번호 0부터 시작, = cap.open(웹캠 오픈)

#나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf')

#무한루프(q를 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, ret true/false
    h, _, _ = frame.shape
    now = datetime.datetime.now()
    currDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    
    if ret != True: break #ret이 false면 루프 탈출

    frame = Image.fromarray(frame) #글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy = (10, (h - 40)), text = '라이브 웹 캠-{0}'.format(currDatetime), font = font, fill = (0, 0, 255)) #xy : 글자가 시작하는 최초 위치
    frame = np.array(frame) #원 상태로 복귀

    cv2.imshow('RealTime CAM', frame) #로드한 영상을 창에 출력

    if cv2.waitKey(1) == ord('q'): #q를 입력하면 루프 탈출
        break

cap.release() # =cap.close(웹캠 해제)
cv2.destroyAllWindows() #메모리 해제    
