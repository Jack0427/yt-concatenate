from .step import Step
from logging import getLogger

class Postflight(Step):
    def __init__(self) -> None:
        pass

    def process(self, data, inputs, utils):
        logger = getLogger()
        if inputs['cleanUp']:
            utils.clean_up_videos_captions_file()
        logger.info('in Postflight')
