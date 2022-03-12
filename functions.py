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

def clip(broken_img):
    try: 
        for rgb_layer in range(3): 
            layer = broken_img[:, :, rgb_layer]
            for row in range(layer.shape[0]): 
                for col in range(layer.shape[1]): 
                    if layer[row][col] < 0:
                        layer[row][col] = 0 
                    elif layer[row][col] > 255:
                        layer[row][col] = 255
            broken_img[:, :, rgb_layer] = layer 
    except: 
        for i in range(len(broken_img)):
            if broken_img[i] < 0:
                broken_img[i] = 0
            elif broken_img[i] > 255:
                broken_img[i] = 255

    plt.title('Clipped Image')
    plt.imshow(broken_img)
    plt.show()
    
    return broken_img

def contrast(image,alpha):
    img=cv.imread(image)
    for i in img:
        for j in i:
            j[0]*=alpha
            j[1]*=alpha
            j[2]*=alpha
    cv2.imwrite('Contrast_Bozu.jpg',img)
    return 'Contrast_Bozu.jpg'


def add_brightness(image,beta):
    img=cv.imread(image)
    for i in img:
        for j in i:
            j[0]+=beta
            j[1]+=beta
            j[2]+=beta
    cv2.imwrite('Bright_Bozu.jpg',img)
    return 'Bright_Bozu.jpg'

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

def apply_threshold(img, threshold):
    img[:, :, :][img[:, :, :] >= threshold] = 255
    img[:, :, :][img[:, :, :] < threshold] = 0
    return img

def clip(broken_image):
    img=cv.imread(broken_image)
    for x in img:
        for y in x:
            if int(y[0])>255:
                y[0]=255
            if int(y[0])<0:
                y[0]=0
            if int(y[1])>255:
                y[1]=255
            if int(y[1])<0:
                y[1]=0
            if int(y[2])>255:
                y[2]=255
            if int(y[2])<0:
                y[2]=0
              
def vintage(img):
    kx = cv.getGaussianKernel(img.shape[0] , 200)
    ky = cv.getGaussianKernel(img.shape[1] , 200)
    kernel = kx * ky.T
    filter = 255 * kernel / np.linalg.norm(kernel)
    img[:, :, 0] = img[:, :, 0] * filter
    img[:, :, 1] = img[:, :, 1] * filter
    img[:, :, 2] = img[:, :, 2] * filter
    return img

def cursed(img):
    kernel = np.array([[-1,-1,-1], 
                      [-1,5,-1], 
                      [0, -1, 0]])
    sharpness = cv.filter2D(src=img, ddepth=-1, kernel=kernel)
    cv.imshow('cursed bozu', sharpness)
    cv.waitKey()
    cv.destroyAllWindows()

def headshot(img):
  x = 0
  y = 0
  height = 450
  width = 750
  cropped = img[y:y+height , x:x+width]
  cv.imwrite("Bozu_headshot.jpg", cropped)

def sepia(img):
  kernel = np.array([[0.393, 0.769, 0.189],
                       [0.349, 0.686, 0.168],
                       [0.272, 0.534, 0.131]])
  sepia_img = cv.transform(img,kernel)  
  return sepia_img

def sharpen(img):
    kernel = np.array([[-1, -1, -1], 
                       [-1, 9.5, -1], 
                       [-1, -1, -1]])
    sharpened_img = cv.filter2D(img, -1, kernel)

    return sharpened_img


def andromeda(picture1,picture2):
    img1=cv.imread(picture1)
    img2=cv.imread(picture2)
    large_img=cv.resize(img1,(1080,720))
    small_img = cv.resize(img2,(300,300))
    x = 400
    y = 170
    x1 = x + small_img.shape[1]
    y1 = y + small_img.shape[0]
    large_img[y:y1,x:x1] = small_img
    cv.imwrite('Galaxy_Bozu.jpg',large_img)

def cartoonify(img):
  blur_img = cv.blur(img ,(5,5))