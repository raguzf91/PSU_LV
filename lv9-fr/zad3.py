import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image


model = tf.keras.models.load_model('best_model.keras')


def prepare_image(img_path, target_size=(64, 64)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  
    return img_array

img_path = 'C:\\Users\\gtsrb\\Test\\20\\01559.png'  

img = prepare_image(img_path)

predictions = model.predict(img)
predicted_class = np.argmax(predictions, axis=1)

print(f"Predicted class: {predicted_class[0]}")

plt.imshow(image.load_img(img_path))
plt.title(f"Predicted class: {predicted_class[0]}")
plt.show()
