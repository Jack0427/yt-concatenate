from .step import Step


class Postflight(Step):
    def __init__(self) -> None:
        pass

    def process(self, data, inputs, utils):
        if inputs['cleanUp']:
            utils.clean_up_videos_captions_file()
        print('in Postflight')
