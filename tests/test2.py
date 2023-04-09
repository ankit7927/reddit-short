from moviepy.editor import concatenate_videoclips

list_clips:list = []

video = open("raw/clips/question.mp4")
list_clips.append(video.buffer)

for i in range(4):
    video = open(f"raw/clips/{str(i)}.mp4")
    list_clips.append(video.buffer)

con = concatenate_videoclips(list_clips)