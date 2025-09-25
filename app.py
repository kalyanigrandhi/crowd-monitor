import streamlit as st
import numpy as np
from PIL import Image

st.title("CSRNet Crowd Counting Demo")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Dummy crowd count (replace with CSRNet later)
    st.success(f"Estimated Crowd Count: {np.random.randint(50,500)}")
else:
    st.info("Please upload an image to start crowd counting.")

