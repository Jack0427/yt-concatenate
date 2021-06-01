from .step import Step
from yt_concatenate.model.found import Found


class Search(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    found.append(Found(yt, caption, time))
        print(len(found))
        return found
