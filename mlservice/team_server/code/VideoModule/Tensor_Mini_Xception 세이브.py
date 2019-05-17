import cv2
import numpy as np
import dlib
import os

from Oracle import Oracle

from keras.models import load_model
from keras.preprocessing.image import img_to_array

def search(dirname):
    #search for n-gram dict file saved
    filenames = os.listdir(dirname)

    result = []
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        result.append(full_filename)
    return result

def make_relative_to_absolute(R_path):
    result = os.path.dirname( os.path.abspath( __file__ ) )
    my_dirs = R_path.split('/')
    for each in my_dirs:
        if each == '.':
            continue
        result = os.path.join(result, each)
        #print('mid term check', result)

    return result

class Tensor_Mini_Xception(Oracle):
    def __init__(self, modelPath, faceClassifierPath):
        print('###################\n', make_relative_to_absolute( faceClassifierPath))
        #print(make_relative_to_absolute(modelPath))

        #print('\n', make_relative_to_absolute( faceClassifierPath))

        self.model = load_model(make_relative_to_absolute(modelPath))
        #self.face_cascade = cv2.CascadeClassifier(make_relative_to_absolute( faceClassifierPath))
        self.face_cascade = cv2.CascadeClassifier('C:\go\haarcascade_frontalface_default.xml')

        self.face_detector = dlib.get_frontal_face_detector()

        #self.model = load_model(modelPath)
        #self.face_cascade = cv2.CascadeClassifier(faceClassifierPath)
        #self.face_detector = dlib.get_frontal_face_detector()


    def predict(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_image, 1.3)#find position of faces

        result = []
        for (fX,fY,fW,fH) in faces:
            roi = gray_image[fY:fY + fH, fX:fX + fW]#cut face image
            roi = cv2.resize(roi, (48, 48))#resize to 48*48(classifier's input size)
            roi = roi.astype("float") / 255.0 #make gray scaler between 0~1
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = self.model.predict(roi)
            result.append(preds)
        return result

    def predict_and_drow(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_image, 1.3)#find position of faces

        result = []
        for (fX,fY,fW,fH) in faces:
            roi = gray_image[fY:fY + fH, fX:fX + fW]#cut face image
            roi = cv2.resize(roi, (48, 48))#resize to 48*48(classifier's input size)
            roi = roi.astype("float") / 255.0 #make gray scaler between 0~1
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = self.model.predict(roi)
            emotion_probability = np.max(preds)
            EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]
            label = EMOTIONS[preds.argmax()]
            cv2.rectangle(image,(fX,fY),(fX+fW,fY+fH),(255,0,0),2)
            cv2.putText(image, label, (fX, fY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            result.append(preds)
        return result, image

    def predict_and_return_others(self, image):

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #print(gray_image)
        faces = self.face_cascade.detectMultiScale(gray_image, 1.3)#find position of faces
        #print(faces)
        #found_faces = self.face_detector(image)#

        #faces = []
        #for f in found_faces:##this can cause face not exist
        #    faces.append([f.left(), f.top(), f.right(), f.bottom()])
        result = []
        for (fX,fY,fW,fH) in faces:
            roi = gray_image[fY:fY + fH, fX:fX + fW]#cut face image
            roi = cv2.resize(roi, (48, 48))#resize to 48*48(classifier's input size)
            roi = roi.astype("float") / 255.0 #make gray scaler between 0~1
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = self.model.predict(roi)
            result.append(preds)

        return result, faces


    def just_drow(self, image, faces, predicted):
        i=0
        for (fX,fY,fW,fH) in faces:
            #emotion_probability = np.max(predicted[i])
            EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]
            label = EMOTIONS[predicted[i].argmax()]
            #cv2.rectangle(image,(fX,fY),(fX+fW,fY+fH),(255,0,0),2)
            cv2.rectangle(image,(fX, fY),(fW, fH),(255,0,0),2)
            cv2.putText(image, label, (fX, fY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            i+=1

    def predict_and_return_others_dlib(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #faces = self.face_cascade.detectMultiScale(gray_image, 1.3)#find position of faces
        #print(faces)
        found_faces = self.face_detector(image)#
        faces = []
        for f in found_faces:
            faces.append([f.left(), f.top(), f.right(), f.bottom()])
        result = []
        for (fX,fY,fW,fH) in faces:
            roi = gray_image[fY:fY + fH, fX:fX + fW]#cut face image
            roi = cv2.resize(roi, (48, 48))#resize to 48*48(classifier's input size)
            roi = roi.astype("float") / 255.0 #make gray scaler between 0~1
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = self.model.predict(roi)
            result.append(preds)

        return result, faces

    def just_drow_dlib(self, image, faces, predicted):
        i=0
        for (fX,fY,fW,fH) in faces:
            #emotion_probability = np.max(predicted[i])
            EMOTIONS = ["angry","disgust","scared", "happy", "sad", "surprised","neutral"]
            label = EMOTIONS[predicted[i].argmax()]
            cv2.rectangle(image,(fX,fY),(fX+fW,fY+fH),(255,0,0),2)
            cv2.putText(image, label, (fX, fY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            i+=1

    def predict_one(self, sliced_gray_image):####???
        preds = self.model.predict(sliced_gray_image)
        return preds


