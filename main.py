import cv2
import matplotlib.pyplot as plt

img = cv2.imread('burung.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

low_range = (100, 100, 100)
high_range = (189, 255, 255)

mask = cv2.inRange(hsv_img, low_range, high_range)
result = cv2.bitwise_and(img, img, mask=mask)

plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.title('Citra Hasil Segmentasi')
plt.imshow(result)
plt.show()