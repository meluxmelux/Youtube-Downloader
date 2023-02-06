from codecs import StreamReader
from distutils.command.sdist import sdist
import sys
import os
from pytube import YouTube

def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    filesize=chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

SAVE_PATH = os.path.dirname(os.path.realpath(__file__)) #"/home/YOURPATH/Downloads"
link = input("Insert your link: ")
outputFileName = input("What is your file name: ")

yt = YouTube(link, on_progress_callback = progress_function)  

yt.streams.filter(progressive = True, 
file_extension = "mp4").get_highest_resolution().download(output_path = "/", filename = outputFileName )

print('Task Completed!')
