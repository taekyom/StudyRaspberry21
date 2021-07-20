import cv2
import numpy as np #c#의 리스트, 행렬이 미포함이므로, numpy 필요

#이미지 로드 기본틀
##이미지 대비 주기
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2) #사이즈 1/2로 축소
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) #먼저 원본을 그레이로 만들고
enhanced = cv2.equalizeHist(gray) #그레이에 대비를 추가

cv2.imshow('original', org) #cv2 새창 열림(이미지를 새창에 띄움)
cv2.imshow('gray', gray)
cv2.imshow('enhance', enhanced) #이미지 대비

cv2.waitKey(0) #창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제