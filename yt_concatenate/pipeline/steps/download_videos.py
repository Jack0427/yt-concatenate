
from pytube import YouTube

from .step import Step
from yt_concatenate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([item.yt for item in data])
        for yt in yt_set:
            if utils.check_file_exists(VIDEOS_DIR+yt.id):
                continue
            try:
                YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
                print('downloading', yt.url)
            except:
                print('Error', yt.url)
        return data
