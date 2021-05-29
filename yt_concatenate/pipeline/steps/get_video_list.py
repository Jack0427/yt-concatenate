import urllib.request
import json
import os

from yt_concatenate.settings import API_KEY
from yt_concatenate.pipeline.steps.step import Step, StepException


class GetVideoList(Step):

    def process(self, data, inputs, utils):
        channelId = inputs.get('channel_id')
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f'{base_search_url}key={API_KEY}&channelId={channelId}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        video_list_path = utils.get_video_list_filepath()
        if utils.check_file_exists(video_list_path):
            video_links = self.read_to_file(video_list_path)
        else:
            while True:
                inp = urllib.request.urlopen(url)
                resp = json.load(inp)

                for i in resp['items']:
                    if i['id']['kind'] == "youtube#video":
                        video_links.append((base_video_url + i['id']['videoId']).strip())

                try:
                    next_page_token = resp['nextPageToken']  # 透過res有沒有該值 沒有就break
                    url = f'{first_url}&pageToken={next_page_token}'
                except:
                    break
            self.write_to_file(video_links,video_list_path)
        return video_links
    
    def write_to_file(self,video_links,filepath):
            with open(filepath, 'a', encoding='UTF-8') as f:
                for context in video_links:
                    f.write(context+'\n')

    def read_to_file(self,filepath):
            with open(filepath, 'r', encoding='UTF-8') as f:
                return f.readlines()