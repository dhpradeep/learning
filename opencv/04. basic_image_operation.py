import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# value of image location
# px = img[55,55]
# print(px)

img[55,55] = [255,255,255]
# print(px)
px = img[55,55]

# ROI = region of image
img[100:150, 100:150] = [255,255,255]

# 74 and 87 is new pixel
watch_face = img[37:111, 107:194]
# image pixel reference to the memory
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
