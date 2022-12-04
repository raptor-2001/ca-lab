from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = plt.imread("flower.jpg")
plt.imshow(image)
plt.axis('off')
plt.show()

# This function tells us that our image is of the type numpy.array.
type(image)

# Printing shape and size of image.
print(image.shape)
print(image.size) # image.size = TOtal number of pixels, w*h*d.

# Retrieving width, height, no_of_channels of an image.
w, h, d = image.shape()

# Now we have normalized 3d image into 2d image.
image_array = image.reshape(w*h, d)
image_array = image_array/255


