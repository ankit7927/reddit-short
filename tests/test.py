import json
import moviepy.editor as mp
from clip import GenerateQuestionCommentClip, GenerateFinalClip

list_clips = []

data:dict = json.load(open("raw/temp.json", "r"))


questClip = mp.VideoFileClip("raw/clips/question.mp4") #GeneateImageClip("raw/images/question.png", "raw/audios/question.mp3", "question")
list_clips.append(questClip)

for i in range(4):
    clip = mp.VideoFileClip(f"raw/clips/{str(i)}.mp4")
    list_clips.append(clip)

title = GenerateQuestionCommentClip(list_clips)

background_clip = mp.VideoFileClip("backgrounds/4.mp4")

GenerateFinalClip([background_clip, title], "testfinal")
