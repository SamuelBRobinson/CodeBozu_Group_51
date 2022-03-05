import matplotlib.image as img
import matplotlib.pyplot as plt
from colorchannels import reddify,greenify,blueify,grayscale,negative

image = img.imread("Bozu.png")
output = image

check = False

while check is False:
    check = True
    input_value = input("Select what you would like to do with your inputted image from the list - Options being \n1:Red channel only\n"
                        +"2:Green channel only\n"+
                        "3:Blue channel only\n"+
                        "4:Grayscale\n"+
                        "5:Negative(inverted)\n")
    if input_value =="1":
        temp = reddify(image)
        plt.imshow(temp)
    elif input_value =="2":
        temp = greenify(image)
        plt.imshow(temp)
    elif input_value =="3":
        temp = blueify(image)
        plt.imshow(temp)
    elif input_value =="4":
        temp = grayscale(image)
        plt.imshow(temp)
    elif input_value =="5":
        temp = negative(image)
        plt.imshow(temp)
    else:
        check = False

plt.show()