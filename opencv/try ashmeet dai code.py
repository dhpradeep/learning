#program for Image Thresholding
import cv2
import numpy as np

# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
image=cv2.imread('image1.JPG',0)
im1 = cv2.resize(image, (1366, 768)) 
cv2.imshow("Original Image", im1)
# gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#lets blur the image first
gray_image=cv2.medianBlur(image,5)

#using adaptive  meanThreshold
thresh=cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,3)
im2 = cv2.resize(thresh, (1366, 768)) 
cv2.imshow("Adaptive Mean Threshold", im2)

#using Thresh Binary
ret, thresh1=cv2.threshold(gray_image, 127,255,cv2.THRESH_BINARY)
im3= cv2.resize(thresh1, (1366, 768))
cv2.imshow("Thresh binary",im3)

_,thresh2=cv2.threshold(gray_image, 127,255,cv2.THRESH_BINARY, cv2.THRESH_OTSU)
im4= cv2.resize(thresh2, (1366, 768))
cv2.imshow("Otsu's Thresholding ", im4)



_,thresh3=cv2.threshold(gray_image, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
im5= cv2.resize(thresh3, (1366, 768))
cv2.imshow("Otsu's Gaussian Thresholding ",im5)

cv2.waitKey()
cv2.destroyAllWindows()
