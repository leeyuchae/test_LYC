import cv2
import numpy as np

# 로컬 이미지 경로 지정
path = "C:\\Users\\ycf20\\OneDrive\\바탕 화면\\cell.png"

# 이미지를 리스트로 관리
images = []

# 이미지 파일을 읽어오기
img_array = np.fromfile(path, np.uint8) # 컴퓨터가 읽을 수 있게 넘파이로 변환
curImg = cv2.imdecode(img_array, cv2.IMREAD_COLOR) # cv2.imdecode는 이미지 배열을 디코딩하여 OpenCV 이미지 형식으로 변환
images.append(curImg)

# 평균 밝기 계산
if images:
    for img in images:
        # 이미지를 그레이스케일로 변환
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 평균 밝기 계산
        mean_brightness = np.mean(gray_img)
        print(f'평균 밝기: {mean_brightness}')
else:
    print('이미지가 리스트에 없습니다.')