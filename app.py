import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🎨 Image to Sketch Converter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert to sketch
    img_array = np.array(image)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    inverted_img = 255 - gray_img
    blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    sketch = cv2.divide(gray_img, 255 - blurred, scale=256)

    st.image(sketch, caption="Pencil Sketch", use_column_width=True)
