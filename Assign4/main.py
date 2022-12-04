import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import time

# Read an image using imread.
img = cv2.imread('image.jpg', 0)

# Resize the image
image = cv2.resize(img, (0,0), None, 0.5, 0.5)

hist = cv2.calcHist([img], [0], None, [256], [0,255])
plt.subplot(111)
plt.plot(hist)
plt.title("Histogram before equalization.")
plt.show()
time.sleep(5)

equ = cv2.equalizeHist(image)

data = Image.fromarray(equ)
data.save('Image_mod.jpg')

# histogram of tube after equalization.
# hist is an array of showing pixels population.

hist1 = cv2.calcHist([equ], [0], None, [256], [0, 255])
plt.subplot(111)
plt.plot(hist1)
plt.title("Histogram after equalization.")
plt.show()

