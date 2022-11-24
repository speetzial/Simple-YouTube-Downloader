# Importing the pytube and moviepy.editor libraries.
import pytube
import moviepy.editor as mp

# This is the code that downloads the video from YouTube.
link = input('Enter your YouTube Link here: ')
dn = pytube.YouTube(link)
print('Download... Please wait...')
video = dn.streams.get_highest_resolution().download()
print('Download successful')
print('')

# Asking the user if they want to convert the video to an MP3 file. If they say yes, it will convert
# Converts the video to an MP3 file.
audioconvert = input('Do you want to convert the video to an MP3 file? (y/n): ')
if audioconvert == 'y':
    clip = mp.VideoFileClip(video).subclip()
    clip.audio.write_audiofile(audio_export.mp3)