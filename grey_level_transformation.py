from PIL import Image
from pylab import *


#读取图像到数组中
im = array(Image.open('F:/Desktop/pcv-book-code-master/ch01/1.png').convert('L'))

im2 = 255-im #对图像进行反向处理
#im3=(100.0/255)*im+100 #将图像像素值变换到100.。。。200区间
#im4=255.0*(im/255.0)**2#对图像像素值求平方后得到的图像

imshow(im)
show()