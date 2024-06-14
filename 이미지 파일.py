from PIL import Image
import numpy as np

# 로컬 이미지 경로 지정
image_path = "C:\\Users\\ycf20\\OneDrive\\바탕 화면\\cell.png"

# 이미지 열기
img = Image.open(image_path)

# 이미지 표시
img.show()

#이미지를 그레이스케일로 변환 : 이미지의 밝기를 계산할 때 각 픽셀의 색상 정보를 단일 밝기 값으로 간소화하기 위함.(0~255 사이의 값) , 계산 단순해짐
gray_image = img. convert("L")

#이미지를 numpy 배열로 변환
image_array = np.array(gray_image)
average_brightness = np.mean(image_array)
print('average_brightness', average_brightness)