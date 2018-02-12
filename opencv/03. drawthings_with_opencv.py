import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

#1st=starting, 2nd=end, 3rd=color(bgr), 4th=lineWidth
cv2.line(img, (0,0), (150,150), (255,0,0), 15)

# draw rectangle
cv2.rectangle(img, (15,25), (200,150), (0,255,0),5)

# draw circle
# 2nd=redius, 3rd=color, 4th=fill in
cv2.circle(img, (100,63), 55, (0,0,255), -1)

#draw polygon
# list of points last_arg= data type
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# true means connect or not last dot
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
# source, name, starting point, font, size, color, thickness,  
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1, (250,205,255), 5, cv2.LINE_AA)

# image is a frame title
cv2.imshow('image', img)

# 0 means any key
cv2.waitKey(0)

cv2.destroyAllWindows()

