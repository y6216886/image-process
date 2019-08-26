import cv2
import numpy as np
img_emboss_input = cv2.imread('2.jpg')
gray = cv2.cvtColor(img_emboss_input, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)                 ##高斯滤波  降噪
ret3,gray_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

kernel_emboss_1 = np.array([[0,-1,-1],
[1,0,-1],
[1,1,0]])
kernel_emboss_2 = np.array([[-1,-1,0],
[-1,0,1],
[0,1,1]])
kernel_emboss_3 = np.array([[1,0,0],
[0,0,0],
[0,0,-1]])
# converting the image to grayscale
# gray_img = cv2.cvtColor(img_emboss_input,cv2.COLOR_BGR2GRAY)
# applying the kernels to the grayscale image and adding the offset to produce the
output_1 = cv2.filter2D(gray_img, -1, kernel_emboss_1) + 128
output_2 = cv2.filter2D(gray_img, -1, kernel_emboss_2) + 128
output_3 = cv2.filter2D(gray_img, -1, kernel_emboss_3) + 128
cv2.imshow('Input', img_emboss_input)
cv2.imshow('Embossing - South West', output_1)
cv2.imshow('Embossing - South East', output_2)
cv2.imshow('Embossing - North West', output_3)
cv2.waitKey(0)