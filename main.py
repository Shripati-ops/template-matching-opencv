import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
x = 0
y = 0
width = 0
height = 0
#template matching in opencv
img_rgb = cv.imread(r"D:\PythonProjects\golfdaddy_divot\trainingimages\730.jpg")

template = cv.imread(os.path.join('./queryImages',"queryImage5.jpg"), cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print(cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2))
    x = pt[0]
    y = pt[1]
    width = w
    height = h
    img_rgb = cv.resize(img_rgb,(580,920))
    print(pt)
    cv.imshow("img1.jpg",img_rgb[pt[0] : pt[0] + w, pt[1] : pt[1] + h])
    # print(x,y,w,h)
# print(img_rgb[341:1586,334:151])
cv.waitKey(0)


# import cv2
# import numpy as np
 
# # Turn on Laptop's webcam
# img_rgb = cv2.imread(r"D:\PythonProjects\golfdaddy_divot\226.jpg")
# # ret, frame = cap.read()

# # Locate points of the documents
# # or object which you want to transform
# pts1 = np.float32([[0, 260], [640, 260],
#                     [0, 400], [640, 400]])
# pts2 = np.float32([[0, 0], [400, 0],
#                     [0, 640], [400, 640]])
    
# # Apply Perspective Transform Algorithm
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# result = cv2.warpPerspective(img_rgb, matrix, (600, 350))
    
# # Wrap the transformed image
# cv2.imshow('frame', img_rgb) # Initial Capture
# cv2.imshow('frame1', result) # Transformed Capture
# cv2.waitKey(0)