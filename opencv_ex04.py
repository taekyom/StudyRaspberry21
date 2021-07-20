import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg', cv2.IMREAD_GRAYSCALE) #이미지 로드, IMREAD_GRAYSCALE : 흑백
dst = cv2.resize(org, dsize=(640, 480))

center = [300, 200] #x, y
color = (0, 0, 255) #red

#1장의 이미지이므로 while-true문이 없음
cv2.circle(dst, tuple(center), 30, color) #원 그리기
cv2.rectangle(dst, (100, 100), (500, 400), (255, 0, 0)) #네모 그리기
cv2.imshow('dest', dst) #이미지 창 띄우기
cv2.waitKey(0)  #키 대기
cv2.destroyAllWindows() #openCV 인스턴스 종료