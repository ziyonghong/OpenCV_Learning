#ROI_test
import cv2 as cv
src=cv.imread('F:/Desktop/image/a.JPG')
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', src)
face = src[200:250, 100:300]    #选择200:250行、100:300列区域作为截取对象
gray = cv.cvtColor(face, cv.COLOR_RGB2GRAY)  #生成的的灰度图是单通道图像
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  #将单通道图像转换为三通道RGB灰度图，因为只有三通道的backface才可以赋给三通道的src
src[200:250, 100:300] = backface
cv.imshow("face", src)
cv.waitKey(0)
cv.destroyAllWindows()