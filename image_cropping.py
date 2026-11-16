import cv2

image = cv2.imread("myOne.png")


if image is None:
            print("Image not found !")
            exit()


print("Original Image shape :",image.shape)

# now for cropping we use numpy slicing array [y1:y2,x1:x2] y or x is the starting or ending postions

cropped_image = image[100:400,50:250]

# for height = 400-100 = 300 and for width 250-50 = 200

# it means start from row 200 and end up at 799 and same start with column 200 and end up with 799 column
# and return the rectangler reigon

print("Cropped Image Shape ",cropped_image.shape)

cv2.imwrite("outputs/cropped_image.png",cropped_image)

cv2.imshow("Original Image",image)
cv2.imshow("Cropped Image",cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()