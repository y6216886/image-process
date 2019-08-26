import os
import shutil

def copy():
    print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
    # path = input ('请键入需要整理的文件夹地址：')
    # new_path = input ('请键入要复制到的文件夹地址：')
    path ="I:/asoct/4channel"
    new_path="G:/CODE/segmentation_of_as_oct/AGAR_code_v1(1)/AGAR_code_v1/data/training100/copy"
    with open("I:/asoct/train4c111.txt",'a') as f:
        for root, dirs, files in os.walk (path):
            for i in range (len (files)):
                print(files[i])
                # f.writelines(files[i])
                # if (files[i][-3:] == 'mat'):
                #     file_path = root + '/' + files[i]
                #     new_file_path = new_path + '/' + files[i]
                #     shutil.copy (file_path, new_file_path)

def insection(path1,path2):
    f1 = open (path1, 'r')
    f2 = open (path2, 'r')
    result1 =[]
    result2= []
    for line in open (path1):
        line = f1.readline ()
        # print(line)
        result1.append (line)
    # print result
    for line in open (path2):
        line = f2.readline ()
        # print(line)
        result2.append (line)
    result3 =list(set(result2).difference(set(result1)))
    f3 = open ("I:/asoct/intersection.txt", 'a')
    for i in result3:
        f3.write(i)
def unionSet(path1, path2):
    result1 = []
    result2 = []
    f1 = open(path1, 'r')
    f2 = open(path2, 'r')
    for line1 in open(path1):
        # print(line1)
        line1 = f1.readline().strip('\n')
        result1.append(line1)
    for line2 in open (path2):
        # print(line2)
        line2 = f2.readline ().strip('\n')
        result2.append(line2)
    print("res1",len(result1))
    print("res2",len (result2))
    result3 = list(set(result1).intersection(set(result2)))
    print(len(result3))
    f3 = open("I:/asoct/uniontrain111.txt", 'a')
    for i in result3:
        f3.write(i+'\n')

if __name__ == '__main__':
    path1 = "C:/Users/PC/Desktop/中山眼科/train_val_test_111/train/train111_withoutpath.txt"
    path2 = "I:/asoct/allFilename_4c111.txt"
    unionSet(path1, path2)



    # path1="I:/asoct/processedfile.txt"
    # path2="I:/asoct/notyet.txt"
    # insection(path1,path2)
    # copy()
    # new_file_path = "G:/CODE/segmentation_of_as_oct/AGAR_code_v1(1)/AGAR_code_v1/data/training100/ASOCT_Image"
    # with open("I:/asoct/intersection.txt") as f:
    #     for filename in f.readlines():
    #         file_path = "I:/octdata/resize/jpg/"+filename.strip('\n')
    #         shutil.copy (file_path, new_file_path)
