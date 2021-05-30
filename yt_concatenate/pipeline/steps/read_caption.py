import os 
from pprint import pprint

from .step import Step
from yt_concatenate.settings import CAPTIONS_DIR

class ReadCaption(Step):
  def __init__(self) -> None:
      pass
    
  def process(self, data, inputs, utils):
    captions_data = {}
    for caption_file in os.listdir(CAPTIONS_DIR):
        captions = {}
        path = os.path.join(CAPTIONS_DIR,caption_file)
        with open(path, 'r', encoding='UTF-8') as f:
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
                  captions[caption] = time  #方便後續搜尋字幕 所以將字幕放在key
          captions_data[caption_file] = captions
    pprint(captions_data)
    return captions_data
