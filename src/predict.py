import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("models/speedbreaker_model.h5")

def predict_image(img_path):

    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)/255
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    if prediction > 0.5:
        return "Speed Breaker"
    else:
        return "Normal Road"