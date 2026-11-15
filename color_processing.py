import cv2
import os

image = cv2.imread("myOne.png")

if image is None:
            print("Image is Not Found")
            exit()

# conversion from BGR TO RGB 

rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # converts to rgb img

grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # bgr to grey img which work best in edge detection and thresholding

# we create outputs directory to save our processed resuts

os.makedirs("outputs",exist_ok=True) # create output directory and save our results

# now save our process images 

cv2.imwrite("outputs/gray_image.png",grey_image)

cv2.imshow("Original Image ",image)
cv2.imshow("Grey_sclae_img",grey_image)

print("Original Image ",image.shape)
print("RGB image ", rgb_image.shape)
print("grey_sclae img",grey_image.shape)

# now inspect specfic pixel value

print("BGR pixel value ",image[100,100])
print("RGB Pixel value ",rgb_image[100,100])
print("grey_sclae img value ", grey_image[100,100])

# grey scale has 1 channel becuase it shows 0 as black and 255 as white and thats how conversion works
# if 50 menas heavy grey if 200 means light grey so like this it converts the img 


cv2.waitKey(0)
cv2.destroyAllWindows()

