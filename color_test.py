import cv2 as cv
import numpy as np


#利用inRange函数过滤视频中的颜色，实现对特定颜色的追踪
def extrace_object_demo():
    capture=cv.VideoCapture("F:/Desktop/image/a.mp4")
    while(True):
        ret, frame = capture.read()
        if ret==False:
            break;
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46]) #设置要过滤颜色的最小值
        upper_hsv = np.array([77,255,255])
        mask= cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv) #调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择绿色区域

        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitKey(40)
        if c == 27:   #按键Esc的ASCII码为27
            break;

#色彩空间的转换
def color_space_demo(image):
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)  #RGB转换为GRAY #这里的生成的gray图是单通道的
    cv.imshow("gray",gray)
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV) #RGB转换为HSV
    cv.imshow("hsv", hsv)
    yuv=cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow(" yuv",  yuv)



src=cv.imread('F:/Desktop/image/a.JPG')
#color_space_demo(src)
#extrace_object_demo()

#通道分离
b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
#最后一个通道设为0
src[:, :, 2] = 0
cv.imshow("changed image", src)
#通道合并
cv.merge([b, g, r])
cv.waitKey(0)
cv.destroyAllWindows()