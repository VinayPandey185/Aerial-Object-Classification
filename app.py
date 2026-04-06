import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model.keras")

st.title("Aerial Object Classification")
st.write("Upload an image to classify it as Bird or Drone")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    label = "Drone" if prediction > 0.5 else "Bird"
    confidence = prediction if prediction > 0.5 else 1 - prediction

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}")