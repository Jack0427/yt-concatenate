from logging import NullHandler
import os

from pytube import YouTube

from yt_concatenate.pipeline.steps.step import Step
from yt_concatenate.utils import Utils


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        i = 0
        for url in data:
            if utils.check_file_exists(utils.get_caption_filepath(url)):
                continue
            i += 1
            if i > 5:  # 只要5個影片就好
                break
            try:
                source = YouTube(url)
                en_caption = source.captions['en'] if 'en' in source.captions else source.captions['a.en']
            except:
                print('download_caption')
            if en_caption:
                en_caption_convert_to_srt = en_caption.generate_srt_captions()

                # save the caption to a file named Output.txt
                with open(utils.get_caption_filepath(url), "w", encoding='UTF-8') as text_file:
                    text_file.write(en_caption_convert_to_srt)
