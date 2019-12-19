import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img = cv2.imread('steamengine.png',)

# converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img1 = cv2.Canny(img,100,200)

plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img1, cmap = 'gray')
plt.title('Edges'), plt.xticks([]), plt.yticks([])

plt.show()
basic