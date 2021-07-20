import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image
from numpy.core.numeric import False_

#카메라 기본 틀
##영상에 글자 출력
cap = cv2.VideoCapture(0) #번호 0부터 시작 +1, = cap.open(웹캠 오픈)

#나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf')

#영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') #H263
is_record = False #녹화중 표시

#무한루프(q를 입력할 때까지)
while True:
    ret, frame = cap.read() #카메라 현재 영상 로드, frame에 저장, ret true/false
    h, w, _ = frame.shape
    now = datetime.datetime.now()
    currDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDatetime = now.strftime('%Y%m%d_%H%M%S')
    
    if ret != True: break #ret이 false면 루프 탈출

    frame = Image.fromarray(frame) #글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy = (10, (h - 40)), text = '라이브 웹 캠-{0}'.format(currDatetime), font = font, fill = (0, 0, 255)) #xy : 글자가 시작하는 최초 위치
    frame = np.array(frame) #원 상태로 복귀

    key = cv2.waitKey(1)
    if key == ord('q'): #q를 입력하면 루프 탈출
        break
    elif key == ord('c'): #c : capture
        cv2.imwrite('./capture/img_{0}.png'.format(fileDatetime), frame)
        print('이미지 저장 완료')
    elif key == ord('r') and is_record == True: #r : 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./capture/record_{0}.avi'.format(fileDatetime), fourcc, 20, (w, h))
        print('녹화 시작')
    elif key == ord('r'): #레코드 종료  
        is_record = False
        video.release()  
        print('녹화 완료')

    if is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius = 5, color = (0, 0, 255), thickness = 3)    
    
    cv2.imshow('RealTime CAM', frame) #로드한 영상을 창에 출력

cap.release() # =cap.close(웹캠 해제)
cv2.destroyAllWindows() #메모리 해제    
