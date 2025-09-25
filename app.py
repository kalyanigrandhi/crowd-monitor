# install prerequisites (run in a notebook cell)
!pip install streamlit -q
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb

# Put the Streamlit app code into a triple-quoted string
app_code = """import streamlit as st
import numpy as np
from PIL import Image

st.title("CSRNet Crowd Counting Demo (Colab + Cloudflare)")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Dummy crowd count (replace with CSRNet later)
    st.success(f"Estimated Crowd Count: {np.random.randint(50,500)}")
else:
    st.info("Please upload an image to start crowd counting.")
"""

# write the app file
with open("app.py", "w") as f:
    f.write(app_code)

# run streamlit in the background (Colab)
get_ipython().system_raw("streamlit run app.py &>/dev/null &")

# give Streamlit time to start before tunnelling
import time
time.sleep(5)

# start cloudflared to expose the local Streamlit port
!cloudflared tunnel --url http://localhost:8501 --no-autoupdate
