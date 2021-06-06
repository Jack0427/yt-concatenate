import os

from yt_concatenate.settings import DOWNLOADS_DIR
from yt_concatenate.settings import VIDEOS_DIR
from yt_concatenate.settings import CAPTIONS_DIR
from yt_concatenate.settings import VIDEO_LIST_NAME
from yt_concatenate.settings import OUTPUT_DIR


class Utils:
    def __init__(self) -> None:
        pass

    def creat_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self):
        return os.path.join(DOWNLOADS_DIR, VIDEO_LIST_NAME)

    def check_file_exists(self, path):
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_output_filepath(self, channel_id, search_word):
        return os.path.join(OUTPUT_DIR, f'{channel_id}_{search_word}.mp4')

    # def show_steps(self, fn):
    #     def wrap():
    #         print(fn.__name__)
    #     return wrap()
