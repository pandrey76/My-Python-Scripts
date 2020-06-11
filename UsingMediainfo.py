
import os
path = os.getcwd()
print(path)

from pymediainfo import MediaInfo
media_info = MediaInfo.parse('my_video_file.mov')
for track in media_info.tracks:
    if track.track_type == 'Video':
        print (track.bit_rate, track.bit_rate_mode, track.codec)
