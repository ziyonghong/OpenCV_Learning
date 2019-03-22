#均值模糊、中值模糊、自定义模糊    模糊是卷积的一种表象
import cv2 as cv
import numpy as np

def blur_demo(image):      #均值模糊  去随机噪声有很好的去燥效果
    dst = cv.blur(image, (1, 15))    #（1, 15）是垂直方向模糊，（15， 1）还水平方向模糊
    cv.namedWindow('blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("blur_demo", dst)

def median_blur_demo(image):    # 中值模糊  对椒盐噪声有很好的去燥效果
    dst = cv.medianBlur(image, 5)
    cv.namedWindow('median_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("median_blur_demo", dst)

def custom_blur_demo(image):    # 用户自定义模糊
    kernel = np.ones([5, 5], np.float32)/25   #除以25是防止数值溢出
    dst = cv.filter2D(image, -1, kernel)
    cv.namedWindow('custom_blur_demo', cv.WINDOW_NORMAL)
    cv.imshow("custom_blur_demo", dst)

src = cv.imread('F:/Desktop/image/a.JPG')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)

blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()