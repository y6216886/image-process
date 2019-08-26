import cv2
import numpy as np

img = cv2.imread("gp.jpg")
cv2.imshow("original", img)

size = 15

kernel_motion_blur = np.zeros((size,size))
print(kernel_motion_blur)
kernel_motion_blur[:,int((size-1)/2)] = np.ones(size)
print(kernel_motion_blur)
kernel_motion_blur = kernel_motion_blur / size
print(kernel_motion_blur)

output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow("motion blur", output)
cv2.waitKey(0)