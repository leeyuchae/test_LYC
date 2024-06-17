import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

def open_multipage_tiff(image_path) :
    images = []
    with Image.open(image_path) as img:
        for frame in ImageSequence.Iterator(img):
            frame = np.array(frame)
            images.append(frame)
    return images

def calculate_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

image_path = 'C:\\Users\\ycf20\\OneDrive\\바탕 화면\\Calcium Imaging.tif'
images = open_multipage_tiff(image_path)

brightness_list = [calculate_brightness(image) for image in images ]
print('calculate_brightness', calculate_brightness)

plt.plot(brightness_list)
plt.title('Average Brightness of Each Image')
plt.xlabel('Image Index')
plt.ylabel('Average Brightness')
plt.show()