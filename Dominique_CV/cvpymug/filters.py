import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('beach.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img1 = cv2.GaussianBlur(img,(5,5),100)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('original')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img1)
plt.title('blurred')
plt.xticks([])
plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
