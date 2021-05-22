import urllib.request
import json
from yt_concatenate.settings import API_KEY

CHANNEL_ID = 'UCwsm-gcz5ZwSLMEr7xA4CHQ'


def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

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


if __name__ == '__main__':
    video_list = get_all_video_in_channel(CHANNEL_ID)
    print(len(video_list), video_list)
