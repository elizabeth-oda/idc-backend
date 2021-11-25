import streamlit as st
from PIL import Image
import numpy as np
import requests
import base64
import tempfile
from idc.processing import split
import requests


# Juxtapose import
# from streamlit_juxtapose import juxtapose
# import pathlib

# STREAMLIT_STATIC_PATH = (
#     pathlib.Path(st.__path__[0]) / "static"
# )  # at venv/lib/python3.9/site-packages/streamlit/static

# IMG1 = "img1.png"
# IMG2 = "img2.png"

you_want = False


st.write("""bro""")

png = st.file_uploader("Upload a PNG image", type=([".png"]))


if png:

    st.image(png)  # display image

    url = "http://127.0.0.1:8000/annotate"

    files = {"file": (png.name, png, "multipart/form-data")}

    # put a spinny wheel while waiting for the response
    response = requests.post(url, files=files)

    st.image(response._content)

    if you_want:
        url = "http://127.0.0.1:8000/predict"

        # preprocessing
        image = Image.open(png)
        array_of_images = split(image)

        bytes_image = base64.b64encode(array_of_images)

        response = requests.post(url, data={"file": bytes_image})

        print(type(response))
