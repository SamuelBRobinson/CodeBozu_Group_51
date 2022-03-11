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
    grayify = 0.2989 * r + 0.5870 * g + 0.1140 * b
    plt.imshow(grayify, cmap='gray')
    plt.show()
    
def negative(img):
    img[:, :, 0] = 255 - img[:, :, 0]
    img[:, :, 1] = 255 - img[:, :, 1]
    img[:, :, 2] = 255 - img[:, :, 2]
    return img

def horizontal_flip(img):
    shape = img.shape
    tempImg = np.zeros([shape[0], shape[1], 3], np.uint8)
    for i in range(shape[1]):
        tempImg[:, i, :] = img[:, shape[1]-i-1, :]
    return tempImg

def vertical_flip(img):
    shape = img.shape
    tempImg = np.zeros([shape[0], shape[1], 3], np.uint8)
    for i in range(shape[0]):
        tempImg[i, :, :] = img[shape[0]-i-1, :, :]
    return tempImg
