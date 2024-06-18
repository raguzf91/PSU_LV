import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

img_original = mpimg.imread(filename)  
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))


plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


model = models.load_model('best_model.keras')


prediction = model.predict(img)
predicted_class = np.argmax(prediction, axis=1)[0]

print(f'Predikcija: {predicted_class}')
