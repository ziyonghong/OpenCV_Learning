import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape);
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    print("w:%s,h:%s,c:%s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv=image[row,col,c]
                image[row,col,c]=255-pv
    cv.imshow("pixels_Demo",image)

def creat_image():
    img=np.zeros([400,400,3],np.uint8)
    img[:, : , 0]=np.ones([400,400])*255
    cv.imshow("new image",img)

def inverse(image):
    dst=cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)

src=cv.imread('F:/Desktop/image/a.JPG')
#cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
#cv.imshow("image",src)
#access_pixels(src)
#creat_image()
inverse(src)
cv.waitKey(0)
cv.destroyAllWindows()