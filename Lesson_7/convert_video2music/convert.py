from moviepy import editor
video = editor.VideoFileClip('convert_video2music/little-me.mp4')
video.audio.write_audiofile('convert_video2music/little-me.mp3')