import cv2

image = cv2.imread("myOne.png")

if image is None:
            print("Image not Found !")
            exit()


print("Original Image Dimenstions",image.shape)

resize_img = cv2.resize(image,(300,500)) # width or height built in resize function

# Shrinking an img
small_img = cv2.resize(image,(600,600),interpolation=cv2.INTER_AREA)

# Enlarging an img
large_img = cv2.resize(image,(2000,2000),interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original Image ",image)
cv2.imshow("Resize Image ",resize_img)

cv2.imwrite("outputs/small.png",small_img)
cv2.imwrite("outputs/large.png",large_img)

print("Resize Image Size :",resize_img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()