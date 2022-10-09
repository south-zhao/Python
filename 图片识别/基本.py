# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/8 16:29
# @Author : south(南风)
# @File : 基本.py
# Describe: 
# -*- coding: utf-8 -*-
import cv2

# img = cv2.imread('title1.jpg', 0)
# cv2.imshow("pic", img)
# key = cv2.waitKey()
# cv2.destroyWindow("pic")
# img1 = cv2.imread('1.jpg', 0)
# img2 = cv2.imread('1.jpg', 1)
# print(img)
# print("=====")
# print(img1)
# print("=====")
# print(img2)

img = cv2.imread('1.jpg', 0)
cv2.imshow("pic", img)
for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255
cv2.imshow("p", img)


key = cv2.waitKey()
cv2.destroyWindow("pic")



