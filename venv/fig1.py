 # -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters


# 添加中文字体支持
from matplotlib.font_manager import FontProperties


im = array(Image.open('F:/Desktop/pcv-book-code-master/ch01/1.png').convert('L'))  # 打开图像，并转成灰度图像

#Sobel导数滤波器
imx=zeros(im.shape)
filters.sobel(im,1,imx)
imshow(im)
show()
