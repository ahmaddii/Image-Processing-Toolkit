import cv2

image = cv2.imread("myOne.png")

if image is None:
            print("Image not found")
            exit()

print("Original Image shape is :",image.shape)

horizental_flip = cv2.flip(image,flipCode=1) # 1 for horizental flip 0 for vertical and -1 for both
vertical_flip = cv2.flip(image,flipCode=0) # 1 for horizental flip 0 for vertical and -1 for both
mix_flip = cv2.flip(image,flipCode=-1) # 1 for horizental flip 0 for vertical and -1 for both

cv2.imwrite("outputs/horizental.png",horizental_flip)
cv2.imwrite("outputs/vertical_flip.png",vertical_flip)
cv2.imwrite("outputs/mix_flip.png",mix_flip)
