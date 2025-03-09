import streamlit as st
from PIL import Image, ImageFilter
import numpy as np
import io

# Function to convert image to sketch
def convert_to_sketch(image):
    # Convert to grayscale
    gray_image = image.convert("L")
    
    # Invert the grayscale image
    inverted_image = Image.eval(gray_image, lambda x: 255 - x)
    
    # Apply Gaussian blur
    blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(radius=21))
    
    # Create the sketch by dividing the grayscale image by the blurred inverted image
    sketch_image = Image.blend(gray_image, blurred_image, alpha=0.5)
    
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

    # Convert to sketch
    sketch_image = convert_to_sketch(image)

    # Display the sketch
    st.image(sketch_image, caption='Sketch Image', use_column_width=True)

    # Convert sketch image to PIL format for download
    buf = io.BytesIO()
    sketch_image.save(buf, format="PNG")
    buf.seek(0)

    st.download_button(
        label="Download Sketch",
        data=buf,
        file_name="sketch.png",
        mime="image/png"
    )
