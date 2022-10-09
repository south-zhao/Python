# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/10/8 16:16
# @Author : south(南风)
# @File : 主颜色.py
# Describe: 
# -*- coding: utf-8 -*-
# import cv2

import numpy as np

import cv2 as cv

image = cv.imread(r'C:\Users\22525\Desktop\Code\Django\static\img\1.jpg')

cv.imshow("input", image)

h, w, ch = image.shape

print((image.shape))
# 构建图像数据
# K-means 只能处理向量形状的数据，不能处理矩阵型数据，
# 这里 reshape(-1, 3) 代表图片的所有像素点，而每个像素点有三个特征（即三个通道）
data = image.reshape((-1, 3))

data = np.float32(data)

# K-means 算法停止条件
# 一个元组，传入 cv.kmeans()，( type, max_iter, epsilon ) type 见下面链接，max_iter 是最大迭代次数，epsilon 要达到的精度
# https://docs.opencv.org/master/d1/d5c/tutorial_py_kmeans_opencv.html

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)

num_clusters = 4  # 聚类的数量

ret, label, center = cv.kmeans(data, num_clusters, None, criteria, 21, num_clusters, cv.KMEANS_RANDOM_CENTERS)

# 生成主色彩条形卡片，大小是：高：50 宽：原图的宽

card = np.zeros((50, w, 3), dtype=np.uint8)

clusters = np.zeros([num_clusters], dtype=np.int32)

for i in range(len(label)):

    clusters[label[i][0]] += 1  # 计算每个类别共有多少个

clusters = np.float32(clusters) / float(h * w)  # 计算概率

center = np.int32(center)  # 因为像素值是 0-255 故对其聚类中心进行强制类型转换

x_offset = 0

for c in np.argsort(clusters)[::-1]:  # 这里对主色按比例从大到小排序 [::-1] 代表首尾反转 如[1,2,3] -> [3, 2, 1]

    dx = np.int(clusters[c] * w)  # 这一类转换成色彩卡片有多宽

    b = center[c][0]  # 这一类对应的中心，即 RGB 三个通道的值

    g = center[c][1]

    r = center[c][2]

    cv.rectangle(card, (x_offset, 0), (x_offset + dx, 50), (int(b), int(g), int(r)), -1)  # 每个主色画出一个矩形

    x_offset += dx  # 偏置就是每个主色的宽度

cv.imshow("color table", card)

cv.waitKey()

cv.destroyAllWindows()



