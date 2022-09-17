# C:\Bin\environment\python
# -*- coding: utf-8 -*-
# @Time : 2022/9/17 14:50
# @Author : south(南风)
# @File : 模糊图像.py
# Describe: 利用scipy库进行图片的模糊处理
# -*- coding: utf-8 -*-
# import numpy as np
# from scipy import signal, misc
# import matplotlib.pyplot as plt
#
# img = misc.face()
# w = np.zeros((50, 50))
# w[0][0] = 1.0
# w[49][25] = 1.0
# img_new = signal.fftconvolve(img, w)
#
# plt.figure()
# plt.imshow(img_new)
# plt.gray()
# plt.title('Img')
# plt.show()

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
image = misc.ascent()#二维图像数组，lena图像
w = np.zeros((50,50))#全0二维数组，卷积核
w[0][0]=1.0#修改参数，调整滤波器
w[49][25]=1.0#可以根据需要调整
image_new = signal.fftconvolve(image, w)#使用FFT算法进行卷积
plt.figure()
plt.imshow(image_new)#显示滤波后的图像
plt.gray()
plt.title('Filtered image')
plt.show()





