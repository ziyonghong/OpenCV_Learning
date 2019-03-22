#高斯模糊    轮廓还在，保留图像的主要特征  高斯模糊比均值模糊去噪效果好
import cv2 as cv
import numpy as  np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv

def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s=np.random.normal(0,20,3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
        cv.namedWindow("noise image", cv.WINDOW_NORMAL)
        cv.imshow("noise image", image)
        #ksize参数表示高斯滤波器模板大小。 ksize.width和ksize.height可以不同，
        # 但它们都必须是正数和奇数。或者，它们可以是零，即（0, 0），然后从σ计算出来。
        dst=cv.GaussianBlur(image,(15,15),0) #高斯模糊
        cv.namedWindow("Gaussian", cv.WINDOW_NORMAL)
        cv.imshow("Gaussian", dst)


src = cv.imread('F:/Desktop/image/a.JPG')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)

gaussian_noise(src)
cv.waitKey(0)
cv.destroyAllWindows()