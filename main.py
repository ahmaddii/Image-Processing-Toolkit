import cv2

image = cv2.imread("myOne.png") # read the image with open cv

cv2.imshow("My First Image ", image) # show the img with open cv 

cv2.waitKey(0) # click 0 to close it 
 
cv2.destroyAllWindows() # and finaly close the img window when 0 click



