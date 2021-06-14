from concurrent.futures import ThreadPoolExecutor
from time import time
from pytube import YouTube
from logging import getLogger

from .step import Step
from yt_concatenate.settings import VIDEOS_DIR

logger = getLogger()


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([item.yt for item in data])
        start = time()
        with ThreadPoolExecutor(max_workers=utils.cpu_count) as executor:
            for yt in yt_set:
                if utils.check_file_exists(VIDEOS_DIR+yt.id):
                    continue
                executor.submit(self.downlaoad_videos, yt)
        end = time()
        spent = end - start
        logger.info(f'download_videos spent {spent} sec')
        return data

    def downlaoad_videos(self, yt):
        try:
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
            logger.info('downloading', yt.url)
        except:
            logger.error('Error', yt.url)
