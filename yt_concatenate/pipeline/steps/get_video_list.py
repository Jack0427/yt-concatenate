import urllib.request
import json

from yt_concatenate.settings import API_KEY
from yt_concatenate.pipeline.steps.step import Step, StepException


class GetVideoList(Step):

    def process(self, data, inputs):
        channelId = inputs.get('channel_id')
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f'{base_search_url}key={API_KEY}&channelId={channelId}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']  # 透過res有沒有該值 沒有就break
                url = f'{first_url}&pageToken={next_page_token}'
            except KeyError:
                break
        return video_links
