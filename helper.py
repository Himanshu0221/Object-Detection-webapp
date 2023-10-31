import os
from ultralytics import YOLO
import streamlit as st
import cv2
import pafy
import tempfile
import settings
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
from pytube import YouTube


def load_model(model_path):
    model = YOLO(model_path)
    return model


def _display_detected_frames(conf, model, st_frame, image):
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))
    
    # Predict the objects in the image using the YOLOv8 model
    res = model.predict(image, conf=conf)
       
    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


def play_youtube_video(conf, model):

    source_youtube = st.sidebar.text_input("YouTube Video url")

    if st.sidebar.button('Detect Objects'):
        try:
            yt = YouTube(source_youtube)
            stream = yt.streams.filter(file_extension="mp4", res=720).first()
            vid_cap = cv2.VideoCapture(stream.url)

            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))



def play_stored_video(conf, model):
    uploaded_file = st.sidebar.file_uploader("Upload a video file", type=["mp4", "avi"])

    if uploaded_file is not None:
        # Create a temporary directory to save the uploaded file
        temp_dir = tempfile.TemporaryDirectory()
        temp_video_path = os.path.join(temp_dir.name, "uploaded_video.mp4")
        with open(temp_video_path, "wb") as video_file:
            video_file.write(uploaded_file.read())

        # Display the uploaded video
        st.video(temp_video_path)

        if st.sidebar.button('Detect Video Objects'):
            try:
                video = cv2.VideoCapture(temp_video_path)
                st_frame = st.empty()

                while video.isOpened():
                    success, image = video.read()
                    if success:
                        _display_detected_frames(conf, model, st_frame, image)
                    else:
                        video.release()
                        break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))

        # Clean up the temporary directory
        temp_dir.cleanup()


def play_webcam(conf, model):
  
    source_webcam = settings.WEBCAM_PATH
    #is_display_tracker, tracker = display_tracker_options()
    if st.sidebar.button('Detect Objects'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))


