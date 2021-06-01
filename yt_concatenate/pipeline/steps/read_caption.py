from .step import Step


class ReadCaption(Step):
    def __init__(self) -> None:
        pass

    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.check_file_exists(yt.caption_filepath):
                continue
            captions = {}
            with open(yt.caption_filepath, 'r', encoding='UTF-8') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        time_line = False
                        captions[caption] = time  # 方便後續搜尋字幕 所以將字幕放在key
            yt.captions = captions
        return data
