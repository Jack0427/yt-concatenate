
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step
from yt_concatenate.settings import OUTPUT_DIR


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)
        # closing VideoFileClips
        for video in clips:
            video.close()
    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time):
        hour, min, sic = time.split(':')
        s, ms = sic.split(',')
        return int(hour), int(min), int(s) + int(ms) / 1000
