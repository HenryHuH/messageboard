# encoding:utf-8
import cv2 as cv
import numpy as np


def get_pos(image):
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    cv.imshow("blurred", blurred)
    canny = cv.Canny(blurred, 80, 400)
    cv.imshow("canny", canny)

    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv.contourArea(contour) < 8000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.imshow('image', image)
            print(x)
            return x
    return 0


if __name__ == '__main__':
    print("begin")
    img0 = cv.imread(r'D:\110.png',0)
    ret, thresh1 = cv.threshold(img0, 180, 255, cv.THRESH_BINARY)
    cv.imshow('thresh1', thresh1)
    print (img0.size)
    #get_pos(img0)
    cv.waitKey(0)
    cv.destroyAllWindows()


    # img = np.ones((200, 200, 3), np.uint8) * 255
    # cv.rectangle(img, (50, 50), (150, 150), (0, 0, 255), 2)
    # cv.imshow('test', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()