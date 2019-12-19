import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
