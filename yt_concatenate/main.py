from yt_concatenate.pipeline.pipeline import Pipeline
from yt_concatenate.pipeline.steps.preflight import Preflight
from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.steps.initialize_yt import InitializeYT
from yt_concatenate.pipeline.steps.download_captions import DownloadCaptions
from yt_concatenate.pipeline.steps.read_caption import ReadCaption
from yt_concatenate.pipeline.steps.search import Search
from yt_concatenate.pipeline.steps.download_videos import DownloadVideos
from yt_concatenate.pipeline.steps.edit_video import EditVideo
from yt_concatenate.pipeline.steps.postflight import Postflight
from yt_concatenate.utils import Utils

CHANNEL_ID = 'UC-qwAKnBVzUlbNwol3UCZIA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'just',
        'limit': 20
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
