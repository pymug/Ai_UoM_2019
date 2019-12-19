import cv2
import matplotlib.pyplot as plt

img = cv2.imread('girl.png')
# cv2.imshow('image',img)

titles = ['original', 'red', 'green', 'blue']

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# split an image into its constituent channels
r, g, b = cv2.split(img1)
images = [cv2.merge((r, g, b)), r, g, b]

plt.subplot(2, 2, 1)
plt.imshow(images[0])
plt.title(titles[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(images[1], cmap='Reds')
plt.title(titles[1])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(images[2], cmap='Greens')
plt.title(titles[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(images[3], cmap='Blues')
plt.title(titles[3])
plt.xticks([])
plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
