import cv2
import numpy as np
import matplotlib.pyplot as plt

# grayscale correspond to 0
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# show in matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100],[80,100], 'c', linewidth=5)
# plt.show()
# show in openCV
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('watchgray.img', img)
