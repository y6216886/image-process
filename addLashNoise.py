import cv2
import random
import numpy as np

def generateLashnoise(path):
    org_img = cv2.imread(path)
    noise = np.array(org_img)
    # noise = np.full((998, 2130), 255, dtype=int)
    ####
    colnoise = np.random.randint (0, 100, size=(998, 20))
    col = random.randint(30,2000)
    for i in range(col, col+20):
        for j in range(998):
            noise[j][i] = colnoise[j][i-col]

    ####
    cv2.imwrite("I:/asoct/addedNoise.jpg", noise)
    cv2.imwrite("I:/asoct/lashNoise.jpg",colnoise)
    
if __name__ == '__main__':
    path = "I:/asoct/20170605.1727702684-1263-1_8.jpg"
    generateLashnoise(path)