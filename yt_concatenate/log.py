import logging
from datetime import datetime
import os


def config_log():
    os.makedirs('log', exist_ok=True)
    now = datetime.now()
    file_name = now.strftime("%m-%d-%Y")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_hanlder = logging.FileHandler(f'log/{file_name}.log')
    file_hanlder.setLevel(logging.INFO)
    file_hanlder.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_hanlder)
    logger.addHandler(stream_handler)
