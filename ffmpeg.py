import subprocess as subp
from os.path import join
from datetime import datetime
import time
dateTimeObj = datetime.now()
 
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H-%M-%S)")
id_test = timestampStr
log_dir = 'c:\\work' # путь куда положить файл с записью
CORE_DIR = 'c:\\Users\\pandr\\ffmpeg-20200315-c467328-win64-static' # путь где лежит ffmpeg.exe
video_file = join(log_dir, 'video_' + id_test + '.flv')

FFMPEG_BIN = join(CORE_DIR, 'bin\\ffmpeg.exe')
command = [
    FFMPEG_BIN,
    '-y',
    '-loglevel', 'error',
    '-f', 'gdigrab',
    '-framerate', '12',
    '-i', 'desktop',
    '-s', '960x540',
    '-pix_fmt', 'yuv420p',
    '-c:v', 'libx264',
    '-profile:v', 'main',
    '-fs', '50M',
    video_file
]
ffmpeg = subp.Popen(command, stdin=subp.PIPE, stdout=subp.PIPE, stderr=subp.PIPE)
time.sleep(10)
ffmpeg.stdin.write("q")
ffmpeg.stdin.close()
