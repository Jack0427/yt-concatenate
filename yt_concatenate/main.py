
from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCwsm-gcz5ZwSLMEr7xA4CHQ'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList()
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
