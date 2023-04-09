from dataExt import DataExtractor
from voice import GenerateVoice
from clip import GeneateImageClip, GenerateFinalClip, GenerateQuestionCommentClip
import os, random

#  https://www.reddit.com/r/AskReddit/comments/12eomgg/whats_a_small_thing_that_makes_you_unreasonably/?sort=new
#  https://www.reddit.com/r/AskReddit/comments/12fykda/what_currently_legal_act_do_you_expect_to_become/

webdriver_opt = """
1. chrome
2. firefox
3. edge
choose browser => """
img_path = "raw/images/"
audio_path = "raw/audios/"
background_path = "backs/"

class Main:
    dataExtractor = None
    page_link:str = None
    clip_list:list = []

    def __init__(self) -> None:
        inp = input(webdriver_opt)
        self.page_link = input("enter page link => ")

        if self.page_link == "":
            raise Exception("page link is required ...")
        
        self.dataExtractor = DataExtractor(inp)
        mainData:dict = self.dataExtractor.extractData(self.page_link)

        self.generateAudios(mainData)

        qnc_clip = self.generateClips(len(mainData["comments"]))

        GenerateFinalClip(qnc_clip, mainData["question"])
    

    def generateAudios(self, mainData:dict):
        GenerateVoice(mainData["question"], "question")

        for inx, i in enumerate(mainData["comments"]):
            GenerateVoice(i, str(inx))
        
    def generateClips(self, comm_len:int):
        question_clip = GeneateImageClip(img_path+"question.png", audio_path+"question.mp3", "question")
        self.clip_list.append(question_clip)

        for i in range(comm_len):
            comment_clip = GeneateImageClip(img_path+str(i)+".png", audio_path+str(i)+".mp3", str(i))
            self.clip_list.append(comment_clip)
        
        return GenerateQuestionCommentClip(self.clip_list)
    

if __name__ == "__main__":
    Main()