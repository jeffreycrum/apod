import os

import requests
import streamlit as st

st.set_page_config(layout="wide")

API_KEY = os.getenv('NASA_API')

nasa_url = ("https://api.nasa.gov/planetary/apod?"
            "date=2025-06-17&"
            f"api_key={API_KEY}")

response = requests.get(nasa_url)
content = response.json()

title = content["title"]
image_url = content["url"]
text = content["explanation"]

image_path = "image.png"
image_resspone = requests.get(image_url)
with open(image_path, "wr") as image:
    image.write(image_resspone.content)


st.title(title)
st.image(image)
st.write(text)