import cv2
import numpy as np
from matplotlib import pyplot as plt


# img= cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
# thresh = 36
# img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
# # img = cv2.imread('gray_image.png',0)
# img = cv2.medianBlur(img,5)
#
# ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
#
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
#
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt


def readpath(path):
    lines = []
    with open(path) as f:
        while (True):
            line = f.readline()
            if not line:
                break
            lines.append(line)
    f.close()
    return lines

class Img:             ##图像平移 旋转 镜像等等
    def __init__(self,image,rows,cols,center=[0,0]):
        self.src=image #原始图像
        self.rows=rows #原始图像的行
        self.cols=cols #原始图像的列
        self.center=center #旋转中心，默认是[0,0]

    def Move(self,delta_x,delta_y):      #平移
        #delta_x>0左移，delta_x<0右移
        #delta_y>0上移，delta_y<0下移
        self.transform=np.array([[1,0,delta_x],[0,1,delta_y],[0,0,1]])

    def Zoom(self,factor):               #缩放
        #factor>1表示缩小；factor<1表示放大
        self.transform=np.array([[factor,0,0],[0,factor,0],[0,0,1]])
    def Vertically(self):                #垂直镜像
        self.transform=np.array([[-1,0,self.rows],[0,1,0],[0,0,1]])
    def Horizontal(self):                #水平镜像
        self.transform=np.array([[1,0,0],[0,-1,self.cols-1],[0,0,1]])



    def Rotate(self,beta):               #旋转
        #beta>0表示逆时针旋转；beta<0表示顺时针旋转
        self.transform=np.array([[math.cos(beta),-math.sin(beta),0],
                                 [math.sin(beta), math.cos(beta),0],
                                 [    0,              0,         1]])

    def Process(self):
        self.dst=np.zeros((self.rows,self.cols),dtype=np.uint8)
        for i in range(self.rows):
            for j in range(self.cols):
                src_pos=np.array([i-self.center[0],j-self.center[1],1])
                # print("src_pos",src_pos)
                # print(self.transform)
                [x,y,z]=np.dot(self.transform,src_pos)
                # print("xyz",x,y,z)
                x=int(x)+self.center[0]
                y=int(y)+self.center[1]

                if x>=self.rows or y>=self.cols or x<0 or y<0:
                    self.dst[i][j]=255
                else:
                    self.dst[i][j]=self.src[x][y]


def noisy(noise_typ,path): ##滤波增加噪声
   image = cv2.imread(path)
   if noise_typ == "gauss":
      # print("yeah")
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   elif noise_typ == "poisson":
          vals = len(np.unique(image))
          vals = 2 ** np.ceil(np.log2(vals))
          noisy = np.random.poisson(image * vals) / float(vals)
          return noisy
   elif noise_typ =="speckle":
          row,col,ch = image.shape
          gauss = np.random.randn(row,col,ch)
          gauss = gauss.reshape(row,col,ch)
          noisy = image + image * gauss
          return noisy

def toguassia(path,filename): ##高斯滤波降噪
    # print("path",path)
    # path = "/home/yangyifan/data/asoct/jpg/20171024.1727702684-5195-1_11.jpg"
    img = cv2.imread(path,0)
    # print(img)
    # global thresholding
    # ret1,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    #
    # # Otsu's thresholding
    # ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # /home/yangyifan/data/asoct/jpg/20171024.1727702684-5195-1_11.jpg
    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow("th",th3)
    # cv2.waitKey(0)
    cv2.imwrite("/home/yangyifan/data/asoct_guassian/"+filename, th3)
if __name__ == '__main__':
    path = "/home/yangyifan/code/jingwen_code_oct_v2/as-oct/test.txt"
    lines = readpath(path)
    for line in lines:
        filename = line.split("/")[-1]
        filename = filename.rstrip ('\n')
        line = line.rstrip("\n")  ##读文件的时候去掉 \n 等字符！！##文件路径
        print(line ,filename)
        # toguassia(line, filename)
        result = noisy("gauss", line)
        cv2.imwrite ("/home/yangyifan/data/asoct_addguassian_noise/" + filename+"noise", result)
        ####

# contours
# image,contours,hierarchy=cv2.findContours(th1,1,2)
# cv2.imshow("image", th3)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# area = cv2.contourArea(contours)
# img=cv2.drawContours(image,[contours[0]],-1,(255,255,0),10)  #标记处编号为0的轮廓


# plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=50)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
#
# for i in range(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
#     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
#     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
#     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
# plt.show()
