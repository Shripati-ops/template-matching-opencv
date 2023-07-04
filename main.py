import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
x = 0
y = 0
width = 0
height = 0
#template matching in opencv
img_rgb = cv.imread(r"D:\PythonProjects\golfdaddy_divot\trainingimages\trainingImage.jpg")
for images in os.listdir("./queryImages"):
    template = cv.imread(os.path.join('./queryImages',images), cv.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        x = pt[0]
        y = pt[1]
        width = w
        height = h
        img_rgb = cv.resize(img_rgb,(600,800))
        cv.imshow('res.png',img_rgb)
print(x,y,width,height)
cv.waitKey(0)
