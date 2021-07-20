import cv2
import numpy as np #c#의 리스트, 행렬이 미포함이므로, numpy 필요

#이미지 로드 기본틀
##이미지 흐리게 하기(blur)
###이미지 선명하게 하기(sharp)
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2) #사이즈 1/2로 축소
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(org, (10, 10)) #이미지 흐리게 변경(숫자가 커질수록 흐려짐)
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharp = cv2.filter2D(org, -1, kernel) #-1 : depth

cv2.imshow('original', org) #cv2 새창 열림(이미지를 새창에 띄움)
cv2.imshow('blur', blur)
cv2.imshow('sharp', sharp)

cv2.waitKey(0) #창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제