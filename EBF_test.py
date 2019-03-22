#边缘保留滤波（EPF）  高斯双边、均值迁移
import cv2 as cv
import numpy as np

def bi_demo(image):   #双边滤波
  #  bilateralFilter(src, d, sigmaColor, sigmaSpace)
  #src :处理的图形   d：在过滤期间使用的每个像素邻域的直径。
  #sigmaColor：色彩空间的标准方差，一般尽可能大。  sigmaSpace：坐标空间的标准方差(像素单位)，一般尽可能小。
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.namedWindow("bi_demo", cv.WINDOW_NORMAL)
    cv.imshow("bi_demo", dst)

def shift_demo(image):   #均值迁移
   # pyrMeanShiftFiltering(src, sp, sr[, dst[, maxLevel[, termcrit]]])
   '''src:输入图像，8位，三通道图像。
     sp:漂移物理空间半径大小。
     sr:漂移色彩空间半径大小。
     dst:和源图象相同大小、相同格式的输出图象。
     maxLevel:金字塔的最大层数。
     termcrit:漂移迭代终止条件。'''

   dst = cv.pyrMeanShiftFiltering(image, 10, 50)
   cv.namedWindow("shift_demo", cv.WINDOW_NORMAL)
   cv.imshow("shift_demo", dst)


src = cv.imread('F:/Desktop/image/a.JPG')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)

bi_demo(src)
shift_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()