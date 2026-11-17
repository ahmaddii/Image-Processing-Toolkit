import cv2

image = cv2.imread("myOne.png")

if image is None:
            print("Image not found !")
            exit()


print("Image shape is : ",image.shape)

rotated_image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

rotated_image_180 = cv2.rotate(image,cv2.ROTATE_180)

rotated_image_anticlockwise = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("outputs/rotated.png",rotated_image)
cv2.imwrite("outputs/rotated_180.png",rotated_image_180)
cv2.imwrite("outputs/rotated_counter_clock.png",rotated_image_anticlockwise)

cv2.imshow("Original Image",image)
cv2.imshow("rotated image",rotated_image)

print("Rotated image shape",rotated_image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
