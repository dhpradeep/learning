import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # hue, saturation, value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,30])
    upper_red = np.array([180,255,150])

    # dark_red = np.uint8([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red, cv2, COLOR_BGR2GRAY)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.filter2D(result, -1, kernel)

    blur = cv2.GaussianBlur(result, (15,15), 0)
    median = cv2.medianBlur(result, 15)
    bilaterial = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    # cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilaterial', bilaterial)
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()


