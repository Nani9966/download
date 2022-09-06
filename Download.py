#code 1
# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:\Ineuron_classes"  # to_do

# link of the video to be downloaded
link = "https://youtu.be/vY8caUaAUUM?list=RDvY8caUaAUUM"

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

# to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')

#code 2 #######################


from pytube import YouTube
yt =YouTube("https://www.youtube.com/watch?v=KZy8um0iY9s")
SAVE_PATH = "E:\Ineuron_classes"  # to_do
yt.streams
yt.streams.filter(progressive=True)
yt.streams.filter(adaptive=True)
yt.streams.filter(only_audio=True)
yt.streams.filter(file_extension='mp4')
stream = yt.streams.get_by_itag(22)
stream.download()
stream.download(SAVE_PATH)

