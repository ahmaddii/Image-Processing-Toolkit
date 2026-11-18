import cv2

image = cv2.imread("myOne.png")

if image is None:
            print("Image not found")
            exit()

print("Original image dimentions is ",image.shape)

blur_3 = cv2.blur(image,(3,3)) # in bracket we have kernal sizes we are calculating average of neighberhood px
blur_5 = cv2.blur(image,(5,5))
blur_16 = cv2.blur(image,(15,15))

guassian_blur = cv2.GaussianBlur(image,(9,9),0)
median_blur = cv2.medianBlur(image,7)

cv2.imwrite("outputs/blur_3.png",blur_3)
cv2.imwrite("outputs/blur_5.png",blur_5)
cv2.imwrite("outputs/blur_16.png",blur_16)
cv2.imwrite("outputs/guassian.png",guassian_blur)
cv2.imwrite("outputs/median.png",median_blur)

# very useful in removal of salt and pepper noise 