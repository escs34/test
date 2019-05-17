import cv2
from pytube import YouTube
import os
import numpy as np

from .Oracle import Oracle
from .Tensor_Mini_Xception import Tensor_Mini_Xception as TMX
from .ImgLoader import ImgLoader

def search(dirname):
    #search for n-gram dict file saved
    filenames = os.listdir(dirname)

    result = []
    for filename in filenames:
        full_filename = dirname + '/' + filename #os.path.join(dirname, filename)
        result.append(full_filename)
    return result

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


def downloadYouTube_if_not_exist(video_url, download_path):
    video_list = search(download_path)
    if len(video_list) == 0:
        print("There's no video with this name. Download start.")
        downloadYouTube(video_url, download_path)
        video_list = search(download_path)
    else:
        print("Video already exist. Loading start")
    return video_list[0]#return video name



class Commander:
    def __init__(self):
        #model_path = './models/my_model.h5'
        model_path = './models/_mini_XCEPTION.61-0.65.hdf5'
        face_detect_model = './haarcascade_files/haarcascade_frontalface_default.xml'
        self.oracle = TMX(model_path, face_detect_model)#Oracle: 
        self.imgLoader = ImgLoader()


    def mainLogic(self, video_url):
        #download
        serial = video_url.split('v=')[1]
        download_path = './videos/'+serial
        print('download path : ', download_path)
        video_name = downloadYouTube_if_not_exist(video_url, download_path)
        print(video_name)
        #downloadYouTube(video_url, download_path) #must be controled by if

        #registing
        print("start registing")
        self.imgLoader.registVideo(video_name)
        print("Video opened at server(Commender).")

        #process (use loop)
        emotion_list = []
        i=0
        print("start extracting")
        faces = []
        while(self.imgLoader.isOpened()):
            i+=1
            #
            img = self.imgLoader.getThisFrame()
            #self.oracle.predict(img)
           
            #print(preds)

            if i % 30 == 1: #1frame per 1 second.
                 #print(i)##
                 preds = None
                 faces = []
                 preds, faces = self.oracle.predict_and_return_others(img)
                 #self.oracle.just_drow(img, faces, preds)#must divide this into class
            if len(faces) != 0:
                self.oracle.just_drow(img, faces, preds)#must divide this into class

            #    _, img = self.oracle.predict_and_drow(img)
            #self.oracle.predict_and_drow(img)
            cv2.imshow("image", img)
            cv2.waitKey(30)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
            #


        cv2.destroyAllWindows()##
        return emotion_list





