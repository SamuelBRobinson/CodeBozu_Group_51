import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def redify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    red = cv.merge([r, blank, blank])
    return red


def greenify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    green = cv.merge([blank, g, blank])
    return green


def blueify(img):
    r, g, b = cv.split(img)
    blank = np.zeros(img.shape[:2], dtype='uint8')
    blue = cv.merge([blank, blank, b])
    return blue


def grayscale(img):
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    grayify = 0.2989 * R + 0.5870 * G + 0.1140 * B
    plt.imshow(imgGray, cmap='gray')
    plt.show()
    
def negative(img):
    img[:, :, 0] = 255 - img[:, :, 0]
    img[:, :, 1] = 255 - img[:, :, 1]
    img[:, :, 2] = 255 - img[:, :, 2]
    return img
