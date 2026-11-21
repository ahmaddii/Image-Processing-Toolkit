import cv2

image = cv2.imread("myOne.png")

if image is None:
            exit()


gray_sclae = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

threshold_value,otsu_image = cv2.threshold(
        gray_sclae,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU # auto determine best threshold value
)

print("Threshold value determined :",threshold_value)
cv2.imwrite("outputs/otsu.png",otsu_image)