from .step import Step


class Postflight(Step):
    def __init__(self) -> None:
        pass

    def process(self, data, inputs, utils):
        print('in Postflight')
