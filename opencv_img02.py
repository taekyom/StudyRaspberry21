import cv2
import numpy as np #c#의 리스트, 행렬이 미포함이므로, numpy 필요

org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2) #IMREAD_GRAYSCALE : 회색으로 출력, cv2.IMREAD_REDUCED_COLOR_2 : 사이즈 1/2로 축소
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2GRAY : 회색으로 출력

h, w, c = org.shape
print('width : {0}, height : {1}, channel : {2}'.format(w, h, c))
size_small = cv2.resize(gray, dsize=(int(w/2), int(h/2))) #dsize=(int(w/2), int(h/2) : w, h를 반으로 줄임(float형태이므로 int로 형변환)

cv2.imshow('original', org) #cv2 새창 열림(이미지를 새창에 띄움) : org 출력
cv2.imshow('gray', gray) #cv2 새창 열림(이미지를 새창에 띄움) : gray 출력
cv2.imshow('Resize', size_small) 

cv2.waitKey(0) #창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제