import cv2
from pytube import YouTube
import os
import numpy as np
import json

from Oracle import Oracle
from Tensor_Mini_Xception import Tensor_Mini_Xception as TMX
from ImgLoader import ImgLoader

#uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

def search(dirname):
    #print(dirname)
    filenames = os.listdir(dirname)
    result = []
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)#dirname + '/' + filename #
        result.append(full_filename)
    return result

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

def downloadYouTube_if_not_exist(video_url, download_path, serial):
    my_download_path = make_relative_to_absolute(download_path)
    my_video_path = make_relative_to_absolute(download_path+'/'+serial)

    video_list = search(my_download_path)
    #print(video_list)

    exist = False
    for each in video_list:
        #print(each)
        if each == my_video_path:#serial:
            exist = True
            #print(exist)
    if exist == False:
        print("There's no video with this name. Download start.")
        #downloadYouTube(video_url, download_path)
        downloadYouTube(video_url, my_video_path)
    else:
        print("Video already exist. Loading start")

    video_list = search(my_video_path)

    return video_list[0]#return video name

def make_relative_to_absolute(R_path):
    result = os.path.dirname( os.path.abspath( __file__ ) )
    my_dirs = R_path.split('/')
    for each in my_dirs:
        if each == '..':# go up
            
        elif each == '.':#current
            continue
        else:#nomal case
            result = os.path.join(result, each)
        #print('mid term check', result)

    return result

class Commander:
    def __init__(self):
        #model_path = './models/my_model.h5'
        model_path = './models/_mini_XCEPTION.61-0.65.hdf5'
        face_detect_model = './haarcascade_files/haarcascade_frontalface_default.xml'
        self.oracle = TMX(model_path, face_detect_model)#Oracle: 
        self.imgLoader = ImgLoader()

    def getEmotionData_per_i_frame(self, video_local_path):
        ####dummy
        pass 

    def secondLogic(self, video_url):#drow all and show, save json
        #download
        serial = video_url.split('v=')[1]
        download_path = './videos'
        print('download path : ', download_path)

        #my_download_path = make_relative_to_absolute(download_path)

        video_name = downloadYouTube_if_not_exist(video_url, download_path, serial)
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
        drowed_image = []
        while(self.imgLoader.isOpened()):
            if i>600:
                break
            i+=1
            #
            if i%500 == 1:
                print(i,'th frame is proceed.')
            img = self.imgLoader.getThisFrame()
            #self.oracle.predict(img)
            #if i==1:
            #    print(img)
            if img is None:
                print('img == None')
                break
            #print(i)
            if True:#i % 15 == 2: #1frame per 1 second. #True:#i>500:#:#
                 #print(i)##
                 preds = [0, 0, 0, 0, 0 ,0 ,0]
                 #faces = []
                 preds, faces = self.oracle.predict_and_return_others(img)
                 #preds = self.oracle.predict(img)
                 #self.oracle.just_drow(img, faces, preds)#must divide this into class

                 for each in preds:
                     emotion_list.append(each)

                 #if preds is not None and len(preds) != 0:#this cause not correct time
                 #    emotion_list.append(preds)

            self.oracle.just_drow(img, faces, preds)#must divide this into class###
            #if len(faces) != 0:#i>530:#this can cause time collapsion
            #    self.oracle.just_drow(img, faces, preds)#must divide this into class

                #pass
            drowed_image.append(img)
            #    _, img = self.oracle.predict_and_drow(img)
            #self.oracle.predict_and_drow(img)

            #cv2.imshow("image", img)
            #cv2.waitKey(30)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
            #
            #if i>530 and i<560:
            #    cv2.imshow("image", img)
            #    cv2.waitKey(30)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
            #if i==560:
            #    cv2.destroyAllWindows()
            #    break

            #
        print('start video')
        print(len(drowed_image))
        would_you_start = input('input anything if you want to start video')
        for each in drowed_image :
            cv2.imshow("image", each)
            cv2.waitKey(45)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
        cv2.destroyAllWindows()##

        would_you_start = input('input anything if you want to start video')
        for each in drowed_image :
            cv2.imshow("image", each)
            cv2.waitKey(45)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
        cv2.destroyAllWindows()##

        would_you_start = input('input anything if you want to start video')
        for each in drowed_image :
            cv2.imshow("image", each)
            cv2.waitKey(45)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
        cv2.destroyAllWindows()##

        would_you_start = input('input anything if you want to start video')
        for each in drowed_image :
            cv2.imshow("image", each)
            cv2.waitKey(45)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
        cv2.destroyAllWindows()##




        print('start making json')
        emotion_array = np.array(emotion_list)
        #print(emotion_array.shape)
        emotion_array = np.transpose(emotion_array)
        #print(emotion_array.shape)
        emotion_average_list = [np.average(each) for each in emotion_array]
        #print(len(emotion_average_list))
        #print(np.array(emotion_average_list).shape)
        #for each in emotion_average_list:
        #    print(each)
        EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]
        emotion_dict_list = []#dict()
        emotion_dict = dict()
        for j in range(len(emotion_average_list)):#(7):
            emotion_dict[ EMOTIONS[j] ] = emotion_average_list[j]
            emotion_dict_list.append( { "label":EMOTIONS[j], "value":emotion_average_list[j] } )

        #print(emotion_dict_list)
        #print('#############')

        #with open('./video_data.json', 'w') as f:
        print(make_relative_to_absolute('./video_data.json'))
        with open(make_relative_to_absolute('./video_data.json'), 'w') as f:
            #dumped = json.dumps(emotion_dict_list)
            #dumped = json.dumps(str(emotion_dict_list))
            #print(dumped)
            #f.write(dumped)
            #f.write('[')
            #for each in emotion_dict_list:
            #    print(each)
            #    f.write( json.dumps(str(each)) )
            #f.write(']')
            #f.write( json.dumps(emotion_dict_list), cls=MyEncoder )
            #f.write( json.dumps(str(emotion_dict)) )
            dumped = json.dumps(str(emotion_dict_list))[1:-1]
            dumped = dumped.replace("'", '"')
            f.write( dumped )


        print('finished')
        #print(len(emotion_list))
        #for each in emotion_list:
        #    print(each)
        return emotion_list










    def mainLogic(self, video_url):
        #download
        serial = video_url.split('v=')[1]
        download_path = './videos'
        print('download path : ', download_path)

        #my_download_path = make_relative_to_absolute(download_path)

        video_name = downloadYouTube_if_not_exist(video_url, download_path, serial)
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
            if i%500 == 1:
                print(i,'th frame is proceed.')
            img = self.imgLoader.getThisFrame()
            #self.oracle.predict(img)
            #if i==1:
            #    print(img)
            if img is None:
                print('img == None')
                break
            #print(i)
            if i % 30 == 2: #1frame per 1 second. #True:#i>500:#:#
                 #print(i)##
                 preds = [0, 0, 0, 0, 0 ,0 ,0]
                 #faces = []
                 preds, faces = self.oracle.predict_and_return_others(img)
                 #preds = self.oracle.predict(img)
                 #self.oracle.just_drow(img, faces, preds)#must divide this into class

                 for each in preds:#this can cause time collapse
                     emotion_list.append(each)

                 #if preds is not None and len(preds) != 0:#this cause not correct time
                 #    emotion_list.append(preds)


            if i>530:#len(faces) != 0:#this can cause time collapsion
                self.oracle.just_drow(img, faces, preds)#must divide this into class
                pass

            #    _, img = self.oracle.predict_and_drow(img)
            #self.oracle.predict_and_drow(img)

            #cv2.imshow("image", img)
            #cv2.waitKey(30)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
            #
            if i>530 and i<560:
                cv2.imshow("image", img)
                cv2.waitKey(30)#pause for 0.010 second 1000:1s = 1000/30=0.33 : 1f
            if i==560:
                cv2.destroyAllWindows()
                break

            #
        print('start making json')
        emotion_array = np.array(emotion_list)
        #print(emotion_array.shape)
        emotion_array = np.transpose(emotion_array)
        #print(emotion_array.shape)
        emotion_average_list = [np.average(each) for each in emotion_array]
        #print(len(emotion_average_list))
        #print(np.array(emotion_average_list).shape)
        #for each in emotion_average_list:
        #    print(each)
        EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]
        emotion_dict_list = []#dict()
        emotion_dict = dict()
        for j in range(len(emotion_average_list)):#(7):
            emotion_dict[ EMOTIONS[j] ] = emotion_average_list[j]
            emotion_dict_list.append( { "label":EMOTIONS[j], "value":emotion_average_list[j] } )

        #print(emotion_dict_list)
        #print('#############')

        #with open('./video_data.json', 'w') as f:
        print(make_relative_to_absolute('./video_data.json'))
        with open(make_relative_to_absolute('./video_data.json'), 'w') as f:
            #dumped = json.dumps(emotion_dict_list)
            #dumped = json.dumps(str(emotion_dict_list))
            #print(dumped)
            #f.write(dumped)
            #f.write('[')
            #for each in emotion_dict_list:
            #    print(each)
            #    f.write( json.dumps(str(each)) )
            #f.write(']')
            f.write( json.dumps(emotion_dict_list), cls=MyEncoder )
            #f.write( json.dumps(str(emotion_dict)) )
            dumped = json.dumps(str(emotion_dict_list))[1:-1]
            dumped = dumped.replace("'", '"')
            f.write( dumped )


        #cv2.destroyAllWindows()##
        print('finished')
        #print(len(emotion_list))
        #for each in emotion_list:
        #    print(each)
        return emotion_list





