import cv2

image = cv2.imread("wowb.jpeg")

if image is None:
            exit()


print("Original Image is ",image.shape)

gray_scale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#ret: Threshold value actually used.
#binary: Resulting thresholded image.

adaptive_mean = cv2.adaptiveThreshold(
        gray_scale,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        11,
        2
)

#adaptive guassian thresholding

adaptive_guassian = cv2.adaptiveThreshold(
        gray_scale,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
)


cv2.imwrite("outputs/adp_mean.png",adaptive_mean)
cv2.imwrite("outputs/adp_guassian.png",adaptive_guassian)
