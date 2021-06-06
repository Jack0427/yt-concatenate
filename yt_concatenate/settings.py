from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")  # my api key
VIDEO_LIST_NAME = 'video_list.txt'

DOWNLOADS_DIR = os.path.join('yt_concatenate', 'downloads')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'cations')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
OUTPUT_DIR = os.path.join('yt_concatenate', 'outputs')
