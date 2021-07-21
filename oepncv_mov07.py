import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

#함수선언 영역
##영상 간의 차이 나는 부분 표시 이미지, 차이 나는 픽셀 개수 리턴함수
def get_diff_image(frame_a, frame_b, frame_c, threshold):
    #세 개의 모든 프레임을 회색으로 변환
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    #a, b 사이 영상 차이값, b, c 사이 영상 차이값 구하기
    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray) #None
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray) #차이가 없을 수도/있을 수도 있음
    
    #영상 차이값이 40이상이면 흰색으로 변경
    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    #두 영상에 공통된 부분을 1로 만듦
    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

    #영상에서 1이 된 부분은 확장해줌(morphology)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt = cv2.countNonZero(diff)

    return diff, diff_cnt

#카메라 기본 틀
##움직임 발생 시 화면 캡처
cap = cv2.VideoCapture(0) #번호 0부터 시작 +1, = cap.open(웹캠 오픈)

#나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf')

#영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') #H263
is_record = False #녹화중 표시

threshold = 40 #영상 차이가 나는 thershold(역치/경계) 설정
diff_max = 10 #영상 차이가 나는 최대 픽셀 수 

#초기 프레임으로 사용할 프레임 최초 저장
ret, frame_a = cap.read()
ret, frame_b = cap.read()

#무한루프(q를 입력할 때까지)
while True:
    now = datetime.datetime.now()
    currDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDatetime = now.strftime('%Y%m%d_%H%M%S')

    #현재 영상 입력
    ret, frame = cap.read() #현재 영상 로드, frame에 저장, ret true/false
    h, w, _ = frame.shape

    if ret != True: break #ret이 false면 루프 탈출

    #현재영상과 초기영상을 비교하여 움직임 인식
    diff, diff_cnt = get_diff_image(frame_a = frame_a, frame_b = frame_b, frame_c = frame, threshold = threshold)
    print(diff_cnt)

    #이미지 개수 차이가 10개 이상이면 움직임이 발생했다고 판단
    if diff_cnt > diff_max :
        #cv2.imwrite('./capture/img_{0}.png'.format(fileDatetime), frame)
        print('움직임 발생! 이미지 캡처 완료')

    #움직임 결과 영상
    cv2.imshow('Diff Result', diff)

    frame_a = np.array(frame_b) #이전화면 이전
    frame_b = np.array(frame) #현재화면 이전
    
    frame = Image.fromarray(frame) #글자출력을 위해 변환
    draw = ImageDraw.Draw(frame)
    draw.text(xy = (10, (h - 40)), text = '라이브 웹 캠-{0}'.format(currDatetime), font = font, fill = (0, 0, 255)) #xy : 글자가 시작하는 최초 위치
    frame = np.array(frame) #원 상태로 복귀

    key = cv2.waitKey(1)
    if key == ord('q'): #q를 입력하면 루프 탈출
        break
    
    cv2.imshow('RealTime CAM', frame) #로드한 영상을 창에 출력

cap.release() # =cap.close(웹캠 해제)
cv2.destroyAllWindows() #메모리 해제    
