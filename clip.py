import moviepy.editor as mp
from moviepy.video.fx.all import speedx, resize
import random, os

def GeneateImageClip(imgPath, audioPath, fileName:str):
    audio = mp.AudioFileClip(audioPath)
    image = mp.ImageClip(imgPath)
    video:mp.VideoClip = image.set_audio(audio)
    video.duration = audio.duration
    video = video.fx(speedx, 1.18)
    video = video.fx(resize, 1.7)
    video.fps = 1
    video.write_videofile("raw/clips/"+fileName+".mp4")
    return video

def GenerateQuestionCommentClip(list_clips:list):
    return mp.concatenate_videoclips(list_clips, method="compose").set_position(lambda t: ('center', 200+t))


def getBackVideo()-> mp.VideoFileClip:
    back_list = os.listdir("backs")
    rend = random.randint(0, len(back_list))
    return mp.VideoFileClip("backs/"+back_list[rend])


def GenerateFinalClip(qncClip:mp.VideoClip, fileName:str):
    background_video = getBackVideo()
    
    if background_video.duration < qncClip.duration:
        background_video = mp.concatenate_videoclips([background_video, background_video, background_video])
    
    background_video = background_video.subclip(0, qncClip.duration)

    final_video = mp.CompositeVideoClip(clips=[background_video, qncClip], use_bgclip=True)

    final_video.write_videofile(f"output/{fileName}.mp4")