import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from del0 import redify,greenify,blueify,negative,grayscale #imports functions from del0 file

img = cv.imread("Bozu.png", 1)
start = False

while start is False:
    start = True
    userInput = input("1: Red-only photo\n" +
           "2: Green-only photo\n" + "3: Blue-only photo\n" + "4: Grayscale photo\n" + "5: Negative photo\n")
    if userInput == "1":
        tempImg = redify(img)
        plt.imshow(tempImg)
    elif userInput == "2":
        tempImg = greenify(img)
        plt.imshow(tempImg)
    elif userInput == "3":
        tempImg = blueify(img)
        plt.imshow(tempImg)
    elif userInput == "4":
        tempImg = grayscale(img)
        plt.imshow(tempImg)
    elif userInput == "5":
        tempImg = negative(img)
        plt.imshow(tempImg)
    else:
        start = False

plt.show()