from concurrent.futures import ThreadPoolExecutor
from time import time
from pytube import YouTube

from yt_concatenate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time()
        with ThreadPoolExecutor(max_workers=utils.cpu_count) as executor:
            for yt in data:
                if utils.check_file_exists(yt.caption_filepath):
                    continue
                executor.submit(self.download_captions, yt)
        end = time()
        spent = end - start
        print(f'download_caption spent {spent} sec')
        return data

    def download_captions(self, yt):
        try:
            source = YouTube(yt.url)
            en_caption = source.captions['en'] if 'en' in source.captions else source.captions['a.en']
            if en_caption:
                en_caption_convert_to_srt = en_caption.generate_srt_captions()

                with open(yt.caption_filepath, "w", encoding='UTF-8') as text_file:
                    text_file.write(en_caption_convert_to_srt)
        except:
            print('download_caption error')
