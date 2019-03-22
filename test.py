from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
#from SciPy import misc

#读取图像到数组中
im = array(Image.open('F:/Desktop/CV/pcv-book-code-master/ch01/1.png').convert('L'))

#绘制图形
imshow(im)

#一些点
x=[100,100,200,200]
y=[200,300,200,300]

#默认为蓝色实线
#plot(x,y)
#使用红色星状标记绘制点
#plot(x,y,'r*')
#带有圆圈标记的绿线
plot(x,y,'go-')

#绘制连接前两个点的线
plot(x[:2],y[:2])

#添加标题，显示绘制的图像
title('Plotting:"1.png')

#不显示坐标轴
#axis('off')
show()