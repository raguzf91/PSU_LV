import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

# Učitavanje slike
image = Image.open('example.png')
image_array = np.array(image)

# Pretvaranje 3D slike u 2D matricu piksela
height, width, depth = image_array.shape
image_array_2d = image_array.reshape((height * width, depth))

# Primjena KMeans algoritma za kvantizaciju boja
n_colors = 8  
kmeans = KMeans(n_clusters=n_colors)
kmeans.fit(image_array_2d)
labels = kmeans.predict(image_array_2d)
centroids = kmeans.cluster_centers_
quantized_image_array_2d = centroids[labels].reshape((height, width, depth))

# Prikaz originalne i kvantizirane slike
plt.figure(figsize=(10, 5))

# Originalna slika
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Originalna slika')
plt.axis('off')

# Kvantizirana slika
plt.subplot(1, 2, 2)
plt.imshow(quantized_image_array_2d.astype(np.uint8))
plt.title('Kvantizirana slika')
plt.axis('off')

plt.show()
