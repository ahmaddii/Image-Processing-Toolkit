import cv2

image = cv2.imread("myOne.png")

if image is None:
            print("Image not found !")
            exit()

print("Image Dimenions or Shape is : ",image.shape)

height,width,channels = image.shape

print("Width",width)
print("Height",height)
print("Channels",channels)

print("Image Data Type ",image.dtype)

# for total no of pixels we  do

print("Total Pixels",width*height)

cv2.imshow("Original Image ",image)

cv2.waitKey(0)

cv2.destroyAllWindows() # open cv loads image in BGR NOT RGB

# for indiviusal pixel you wanted to explore you can do it like mentioning specific row or column

pixel = image[100,100]

print("Specfic Pixel Value is ",pixel)