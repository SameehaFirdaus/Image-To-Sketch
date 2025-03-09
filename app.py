import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# Function to convert image to sketch
def convert_to_sketch(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_image = 255 - gray_image
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    # Create the sketch
    sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)
    return sketch_image

# Streamlit app
st.title("Image to Sketch Converter")
st.write("Upload an image and convert it to a sketch!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to a format suitable for OpenCV
    image_array = np.array(image)
    
    # Convert to sketch
    sketch_image = convert_to_sketch(image_array)

    # Display the sketch
    st.image(sketch_image, caption='Sketch Image', use_column_width=True)

    # Convert sketch image to PIL format for download
    sketch_pil = Image.fromarray(sketch_image)

    # Create a download button
    buf = io.BytesIO()
    sketch_pil.save(buf, format="PNG")
    buf.seek(0)

    st.download_button(
        label="Download Sketch",
        data=buf,
        file_name="sketch.png",
        mime="image/png"
    )
