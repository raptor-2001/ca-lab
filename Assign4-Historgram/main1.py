import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

flower = cv2.imread("image.jpg")
flower = cv2.resize(flower, (800, 600))

flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.10, beta=-20)
s = flowerGray.shape
# cv2.imshow('GrayScale', flowerGray)


def Hist(image):
    s = image.shape
    H = np.zeros(shape=(256,1))
    for i in range(s[0]):
    	for j in range(s[1]):
    	    k = image[i, j]
    	    H[k,0] = H[k,0]+1
    return H
    
H = Hist(flowerGray)
plt.plot(H)
plt.show()

# From here equalization of histogram starts.
x = H.reshape(1, 256)

y = np.array([])
y = np.append(y, x[0,0])

for i in range(255):
    k = x[0, i+1] + y[i]
    y = np.append(y, k)
   
y = np.round((y/(s[0]*s[1])) * 255)
for i in range(s[0]):
    for j in range(s[1]):
    	k = flowerGray[i,j]
    	flowerGray[i,j] = y[k]
    	
# cv2.imshow('Normalized', flowerGray)
# cv2.waitKey(0)
equalizehist = Hist(flowerGray)
plt.plot(equalizehist)
plt.show()
