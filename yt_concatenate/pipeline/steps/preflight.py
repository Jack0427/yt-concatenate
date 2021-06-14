from logging import getLogger
from .step import Step


class Preflight(Step):
    def __init__(self) -> None:
        pass

    def process(self, data, inputs, utils):
        logger = getLogger()
        logger.info('in Preflight')
        utils.creat_dirs()
