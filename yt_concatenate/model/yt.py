import os

from yt_concatenate.settings import CAPTIONS_DIR
from yt_concatenate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, f'{self.id}.txt')

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, f'{self.id}.txt')

    def __str__(self) -> str:
        return f'<YT id={self.id}>'

    def __repr__(self) -> str:
        return f'url={self.url} : id={self.id}'
