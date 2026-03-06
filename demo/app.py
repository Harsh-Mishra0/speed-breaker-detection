import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("models/speedbreaker_model.h5")

st.title("Speed Breaker Detection")

uploaded_file = st.file_uploader("Upload Road Image")

if uploaded_file:

    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

    img = img.resize((224,224))
    img = np.array(img)/255
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    if prediction > 0.5:
        st.success("Speed Breaker Detected")
    else:
        st.info("Normal Road")