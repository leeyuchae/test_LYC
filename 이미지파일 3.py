import cv2

image_path = "C:\\Users\\ycf20\\OneDrive\\바탕 화면\\cell.png"
image = cv2.imread(image_path)
cv2.imshow('image',image)
cv2.waitkey(0)