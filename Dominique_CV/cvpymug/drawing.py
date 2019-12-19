import numpy as np
import cv2

img = cv2.imread('people.png', cv2.IMREAD_COLOR)

cv2.rectangle(img,(584,0),(810,128),(0,255,0),3)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
