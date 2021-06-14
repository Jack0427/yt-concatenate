import sys
import getopt

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


def print_usage():
    print('OPTIONS:')
    print('{:>5} {:<15} {}'.format('-h', 'help', 'provide information'))
    print('{:>5} {:<15} {}'.format('-r', '', 'clean up videos and captions file'))
    print('{:>5} {:<15} {}'.format('-l', '', 'Maxmum number of videos clip'))
    print('{:>5} {:<15} {}'.format('', 'channelId', 'The Youtube channel id you want to search for'))
    print('{:>5} {:<15} {}'.format('', 'searchWord', 'The word you want to search for'))


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'just',
        'limit': 20,
        'cleanUp': False
    }

    argv = sys.argv[1:]
    short_args = 'hrl:'
    long_args = 'channelId= searchWord= help='.split()

    try:
        opts, args = getopt.getopt(argv, short_args, long_args)
    except:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_usage()
            sys.exit()
        if opt == '-r':
            inputs['cleanUp'] = True
        if opt == '-l':
            inputs['limit'] = int(arg)
        if opt == '--channelId':
            inputs['channel_id'] = arg
        if opt == '--searchWord':
            inputs['search_word'] = arg

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
