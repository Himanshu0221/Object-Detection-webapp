import streamlit as st
import base64

import base64


# Set the app title and icon
st.set_page_config(
    page_title="Object Detection App",
    page_icon="🕵️‍♀️",
    layout="wide",
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image5.jpeg') 

# Title and description
st.title("Object Detection & Segmentation")
st.write("Welcome to the Object Detection & Segmentation Web App.")

# Home content
st.markdown(
    """
    This web app allows you to perform object detection and segmentation tasks using various sources.
    - **Image Detection:** Upload an image for object detection.
    - **Video Detection:** Upload a video for object detection.
    - **Real-Time Detection:** Perform real-time object detection from your webcam stream.
    """
)