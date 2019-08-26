import scipy.io as scio
import numpy as np
import cv2
import json
import shutil
import os
import shutil
from PIL import Image


def readcoordination(path):
    labels = scio.loadmat (path)
    # print(labels)
    curves = labels['Curve']
    top_iris_y=curves["top_iris_y"]
    bot_iris_y = curves["bot_iris_y"]
    bot_cornea_y =curves["bot_cornea_y"]
    # print(top_iris_y)
    return top_iris_y, bot_iris_y,  bot_cornea_y


def copySpecFile():
    allMatfile=[]
    # print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
    # path = input ('请键入需要整理的文件夹地址：')
    # new_path = input ('请键入要复制到的文件夹地址：')
    path = "G:/CODE/segmentation_of_as_oct/AGAR_code_v1(1)/AGAR_code_v1/data/training100/copy"
    # new_path = "G:/CODE/segmentation_of_as_oct/AGAR_code_v1(1)/AGAR_code_v1/data/training100/copy1"
    for root, dirs, files in os.walk (path):
        for i in range (len (files)):
            # print(files[i])
            if (files[i][-3:] == 'mat'):
                file_path = root + '/' + files[i]
                # new_file_path = new_path + '/' + files[i]
                # shutil.copy (file_path, new_file_path)
                filename=files[i]
                allMatfile.append([file_path,filename])
    return allMatfile
def generateCoordination(array1, array2, array3, img, filename):
    # print(array3.shape)
    # print(img.shape)
    for i in range(2130):
        try:
        # print("array3",array3[i])
            img[min(int(array1[i]),997), i] = 255
            # img[array2[i],i] = 100
            img[min(int(array3[i]),997), i] = 255
        except:
            continue
        # img[array3[i], i] = 255
    # print(img.shape)
    # cv2.imshow ("img", img)
    # cv2.waitKey (0)
    # cv2.imwrite("I:/asoct/+"+filename+".jpg", img)
    return img

def concateImage(path, filename, imgc1):
    imgc3 = cv2.imread(path)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    print("imgc3",path )
    img = np.zeros((998, 2130, 4))
    img[:, :, 0] = imgc3[:, :, 0]
    img[:, :, 1] = imgc3[:, :, 1]
    img[:, :, 2] = imgc3[:, :, 2]
    img[:, :, 3] = imgc1
    # print(img[:, :, 3])
    cv2.imwrite("I:/asoct/4channel/"+filename+".png", img)
def sample_image_name(path):
    img = np.array(Image.open(path))
    cv2.imwrite("I:/3channel.png",img[:,:,3])

def paintCoordination(mat=[]):
    img=np.zeros((998,2130))
    cv2.imshow("img", img)
    cv2.waitKey(0)

def read_json():
    with open("err_1500.json", "r") as f:
        temp = json.loads(f.read())["err_name_list"]
    return temp


def objFileName():
    filename=read_json()
    return filename


def copy_img():
    local_img_name = r'I:/octdata/resize/jpg'
    # 指定要复制的图片路径
    path = r'I:/octdata/resize/err_img'
    # 指定存放图片的目录
    for i in objFileName():
        print(i[0])
        shutil.copy (local_img_name + '/' + i[0], path + '/' + i[0])
def concateee():
    edge_img = cv2.imread (os.path.join (ROOT_DIR, 'datasets/knifes/train/edges/000001_20180328_00000355.BMP'), 0)
    raw_img = cv2.imread (os.path.join (ROOT_DIR, 'datasets/knifes/train/images/000001_20180328_00000355.BMP'))

    edge_img = edge_img.reshape ((edge_img.shape[0], edge_img.shape[1], 1))
    print(edge_img.shape)
    img = np.concatenate ((raw_img, edge_img), 2)
    print(img.shape)

if __name__ == '__main__':
    matfile = copySpecFile()
    for path, filename in matfile:
        ty,by,bc=readcoordination(path)  ##path for .mat file
        #paintCoordination()
        img = np.zeros ((998, 2130))
        # print(img)
        # print("y",ty[0][0][0])
        ty=ty[0][0][0]
        by=by[0][0][0]
        bc=bc[0][0][0]
        imgc1=generateCoordination(ty,by,bc,img,filename)
        ########
        filename = filename[:-12]
        print(filename)
        imgpath = "I:/octdata/resize/jpg/"+filename+".jpg"##path for origin image_file
        concateImage(imgpath, filename, imgc1)

    #
    # path = "I:/asoct/4channel/20170418.1727702684-101-1_12.png"
    # sample_image_name(path)
