from cv2 import blur
import matplotlib.image as mping
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from functions import redify,greenify,blueify,negative,grayscale,horizontal_flip, cursed,vertical_flip,vintage,headshot,sepia,sharpen,cartoonify,apply_threshold,clip,andromeda #imports functions from del0 file

img = cv.imread("Bozu.png", 1)
#img = cv.imread("real-hippo.jpg",1)
start = False

while start is False:
    start = True
    userInput = input("""
    
    1: Red-Only Image
    2: Green-Only Image
    3: Blue-Only Image
    4: Grayscale Image
    5: Negative Image
    6: Horizontal Flip
    7: Vertical Flip
    8: Vintage Filter




    9: C̸̱͚̪̺̠̃̂̌̓̄͋͆̔̔̅̾͝u̶̡̹͌͗͛̕͝r̶̯̥̰̈́̍͒̂̓̅̔͌̓̈́̍̎͒s̸̨̧̛̟̼̱͍̅̀̎́͑̉͒̎̅͋̋͜ȩ̷͈̱̗͈̤͚̪̣̝̠́͐̃͗̈́̏̐͐̉̀̋̂̅̽͐d̵̯̭̳̝̥̲̈̾̋̀̾́̅̄̓̍́͂̒͝ ̴̹͙̗̬͍̤̪̹̜̙̻̜̝͙̈͒̿Ḟ̴̨̡̢̯͕̬̤̖̀̓͂͐̊͌͝͝į̷̗̮̟͖̘̭̠͉̱͔̰̯̈̈́̋͒͑̅̍͒̉ḽ̸̛̛̛̰͑̓͊͑͆͛̈͗͑̈́̋͠ť̶̛̫̻̾̄͑̂͝e̸͎̥̿̀̍̿̈́̅̓͛̿̐̉̊͐͘̚ŕ̴̢̡̛̪͔̰̦͎̈̍̋̾̕


    10: Sepia Filter
    11: Sharpen Image
    12: Threshold
    13: Andromeda
    """) #12 is other for our test runs
    
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
    elif userInput == "6":
        tempImg = horizontal_flip(img)
        plt.imshow(tempImg)
    elif userInput == "7":
        tempImg = vertical_flip(img)
        plt.imshow(tempImg)
    elif userInput == "8":
        tempImg = vintage(img)
        plt.imshow(tempImg)
    elif userInput == "9":
        tempImg = cursed(img)
        plt.imshow(tempImg)
    elif userInput == "10":
        tempImg = sepia(img)
        plt.imshow(tempImg)
    elif userInput == "11":
        tempImg = sharpen(img)
        plt.imshow(tempImg)
    elif userInput == "12":
        threshold = int(input("Enter threshold:"))
        tempImg = apply_threshold(img,threshold)
        plt.imshow(tempImg)
    elif userInput == "13":
        picture1 = cv.imread("andromeda_galaxy.jpg")
        picture2 = cv.imread("Bozu.png")
        tempImg = andromeda(picture1,picture2)
        plt.imshow(tempImg)
    else:
        start = False

plt.show() 