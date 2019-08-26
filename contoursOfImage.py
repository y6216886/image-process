import cv2
import numpy as np

def bestMethodByNow(path):
    img = cv2.imread (path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold (gray,127, 255, cv2.THRESH_BINARY)
    # cv2.imshow ("img", binary)
    # cv2.waitKey(0)
    blur = cv2.GaussianBlur(gray,(5,5),0)                 ##高斯滤波  降噪
    ret3,binary = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow ("img", img)
    # cv2.waitKey(0)

    kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])               #锐化   加强边缘
    binary = cv2.filter2D(binary, -1, kernel_sharpen_2)

    # image, contours, hierarchy= cv2.findContours (binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours (img, contours, -1, (0, 0, 255), 3)



    # for i in contours:
    #     print(contours)
    cv2.imshow ("img", binary)
    cv2.waitKey(0)

def get_all_contours(path):
    img = cv2.imread(path)
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    # Find all the contours in the thresholded image. The values
    # for the second and third parameters are restricted to a
    # certain number of possible values.
    im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, \
    cv2.CHAIN_APPROX_SIMPLE )
    return contours

if __name__ == '__main__':
    path = "I:/concate/1.jpg"
    # bestMethodByNow(path)
    img  = cv2.imread(path)
    contour = get_all_contours(path)
    cv2.drawContours(img, contour,-1,(255,0,0),3)
    cv2.imshow("ss", img)
    cv2.waitKey(0)