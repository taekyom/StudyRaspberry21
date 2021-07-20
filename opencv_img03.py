import cv2
import numpy as np #c#의 리스트, 행렬이 미포함이므로, numpy 필요

#이미지 로드 기본틀
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2) #사이즈 1/2로 축소
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape

#이미지 자르기
#cropped = org[:, :int(w/2)] #[높이, 넓이](생략시 처음 상태 유지)
cropped = gray[:int(h/2), :] #[높이, 넓이](생략시 처음 상태 유지)

cv2.imshow('original', org) #cv2 새창 열림(이미지를 새창에 띄움)
cv2.imshow('cropped', cropped) #반으로 자른 이미지

cv2.waitKey(0) #창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제