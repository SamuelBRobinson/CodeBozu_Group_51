import numpy as np
import cv2 

def reddify(image):
    r,g,b = cv2.split(image)
    blank = np.zeros(image.shape[:2], dtype='uint8') # removes all colour from selected channel
    red=cv2.merge([r,blank,blank]) 
    return red

def greenify(image):
    r,g,b = cv2.split(image)
    blank = np.zeros(image.shape[:2], dtype='uint8')
    green=cv2.merge([blank,g,blank])
    return green

def blueify(image):
    r,g,b = cv2.split(image)
    blank = np.zeros(image.shape[:2], dtype='uint8')
    blue= cv2.merge([blank,blank,b])

def grayscale(image):
    r,g,b = cv2.split(image)
    output = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return output

def negative(image):
    r,g,b = cv2.split(image)
    r = 255 - r
    g = 255 - g
    b = 255 - b 
    output = cv.merge([r,g,b])
    return output