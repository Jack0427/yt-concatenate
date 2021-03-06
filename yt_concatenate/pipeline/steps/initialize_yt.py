from .step import Step
from yt_concatenate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url.replace('\n', ''))for url in data]
