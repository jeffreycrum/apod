import os

import requests
import streamlit as st

st.set_page_config(layout="wide")
st.header("This is NASA's image of the day")

API_KEY = os.getenv('NASA_API')

nasa_url = ("https://api.nasa.gov/planetary/apod?"
            "date=2025-06-17&"
            f"api_key={API_KEY}")

response = requests.get(nasa_url)
content = response.json()

image_url = content["url"]
text = content["explanation"]

image_res = requests.get(image_url)
image = image_res.content

st.image(image)
st.write(text)