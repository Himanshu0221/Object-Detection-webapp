from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
YOUTUBE = 'YouTube'
SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'office_4.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'office_4_detected.jpg'

# Define the directory where video files are stored
VIDEO_DIR = ROOT / 'videos'
DEFAULT_VIDEO = VIDEO_DIR / 'video (2160p).MP4'
#DEFAULT_DETECT_VIDEO = VIDEO_DIR / 

# # Create an empty dictionary to store video paths
# VIDEOS_DICT = {}

# # Iterate through the video directory and add video files to the dictionary
# for video_file in VIDEO_DIR.iterdir():
#     if video_file.is_file() and video_file.suffix in ['.mp4', '.avi', '.mov']:
#         video_name = video_file.stem
#         VIDEOS_DICT[video_name] = video_file

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0