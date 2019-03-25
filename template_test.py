#模板匹配
import cv2 as cv
import numpy as np
def template_demo():
    tpl =cv.imread('F:/Desktop/image/target.JPG')
    image = cv.imread("F:/Desktop/image/a.JPG")
    cv.namedWindow('template image', cv.WINDOW_NORMAL)
    cv.imshow("template image", tpl)
    cv.namedWindow('target image', cv.WINDOW_NORMAL)
    cv.imshow("target image", image)
    #TM_SQDIFF_NORMED是标准(归一化)平方差匹配;TM_CCORR_NORMED是标准相关性匹配;TM_CCOEFF_NORMED是标准相关性系数匹配
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]   #3种模板匹配方法
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(image, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)   #br是矩形右下角的点的坐标
        cv.rectangle(image, tl, br, (0, 0, 255), 2)
        cv.namedWindow("match-" + np.str(md), cv.WINDOW_NORMAL)
        cv.imshow("match-" + np.str(md),image)

template_demo()
cv.waitKey(0)
cv.destroyAllWindows()