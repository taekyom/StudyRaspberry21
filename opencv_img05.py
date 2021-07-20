import cv2
import numpy as np #c#의 리스트, 행렬이 미포함이므로, numpy 필요

#이미지 로드 기본틀
##이미지 노이즈 추가
org = cv2.imread('./image/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2) #사이즈 1/2로 축소
h, w, c = org.shape
noise = np.uint8(np.random.normal(loc = 0, scale = 50, size = [h, w, c])) #noise 정도 설정
noised_img = cv2.add(org, noise) #원본 이미지에 노이즈 추가

cv2.imshow('original', org) #cv2 새창 열림(이미지를 새창에 띄움)
cv2.imshow('noise', noised_img)

cv2.waitKey(0) #창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제