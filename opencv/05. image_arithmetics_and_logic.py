import cv2
import numpy as np

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')
img3 = cv2.imread('watch.jpg')

# add = img1 + img2

# cv2.add = add all pixels
# add = cv2.add(img1, img2)

# pixel are divided into percentage opacity 1st is 60% and 2nd is 40%, last is gamma
# weighted = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
# cv2.imshow('add', weighted)

rows,cols,channels = img3.shape
#roi = region of image
roi = img1[0:rows, 0:cols]
# mask in initial conversion to grayscale
img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('mask',mask)

# bitwise = low level logical operation
mask_inv = cv2.bitwise_not(mask)
# cv2.bitwise_and, cv2.bitwise_or, cv2.bitwise_xor

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img2_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
