import cv2
import numpy as np
from PIL import Image

class process():
    def __init__(self, path):
        self.path = path     ##文件路径
        self.avg_col = []    ##图像每一列的平均值
        self.Area = []       ##artifact所在的列索引

    def findArtifact(self, threshold):
        img = cv2.imread(self.path)
        img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sum2 = 0
        for i in range(len(img[0])):
            sum1 = 0
            for j in range(len(img)):
                sum1 += img[j][i]
                sum2 += img[j][i]
            self.avg_col.append(sum1/len(img))      ##计算每一列的平均intenisty

        avg_all = sum2/(len(img)*len(img[0]))     ##整个图像的平均强度  标量
        print(avg_all)
        print(len(self.avg_col))

        for i in range(len(self.avg_col)):
            if (abs(self.avg_col[i] - avg_all) > threshold):     ##超参数  判断artifact
              self.Area.append(i)

    def remove(self):                                       ##去除artifact的函数
        img = cv2.imread (self.path)
        img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
        for i in self.Area:
            print(i)
            for j in range(len(img)):
                img[j][i] -= 50*self.avg_col[i]
        return img


if __name__ == '__main__':
    pro = process("4.jpg")
    pro.findArtifact(30)
    img = pro.remove()
    cv2.imshow("img",img)
    cv2.waitKey(0)
    ##效果不够好，什么原因