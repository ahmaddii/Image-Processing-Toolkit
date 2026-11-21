import cv2

image = cv2.imread("myOne.png")

if image is None:
            exit()


print("Original Image is ",image.shape)

gray_scale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

threshold_value = 127

#ret: Threshold value actually used.
#binary: Resulting thresholded image.

ret,binary = cv2.threshold(
        gray_scale,
        threshold_value,
        255, # maximum intensity
        cv2.THRESH_BINARY
)

print("Threshold value used ",ret)

cv2.imwrite("outputs/gray_scale.png",gray_scale)
cv2.imwrite("output/binary_thres.png",binary)

cv2.imshow("Binary_Threshold",binary)

cv2.waitKey(0)
cv2.destroyAllWindows()