from logging import NullHandler
import os

from pytube import YouTube

from yt_concatenate.pipeline.steps.step import Step
from yt_concatenate.utils import Utils


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        i = 0
        for yt in data:
            if utils.check_file_exists(yt.caption_filepath):
                continue
            i += 1
            if i > 5:  # 只要5個影片就好
                break
            try:
                source = YouTube(yt.url)
                en_caption = source.captions['en'] if 'en' in source.captions else source.captions['a.en']
                if en_caption:
                    en_caption_convert_to_srt = en_caption.generate_srt_captions()

                    # save the caption to a file named Output.txt
                    with open(yt.caption_filepath, "w", encoding='UTF-8') as text_file:
                        text_file.write(en_caption_convert_to_srt)
            except:
                print('download_caption error')
        return data
