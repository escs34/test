import cv2


class ImgLoader:
    '''Return 1 frame of video
    '''
    def __init__(self):
        #self.cap = ##initialize member variable
        self.vidcap = None
        #pass

    def registVideo(self, path):
        #Open Video by parameter path (string type)
        self.vidcap = cv2.VideoCapture(path)
        #pass

    def getThisFrame(self):
        #Return current 1 frame
        ret, image = self.vidcap.read()
        return image
        #pass

    def isOpened(self):
        return self.vidcap.isOpened()

if __name__ == '__main__':
    imgLoader = ImgLoader()
    imgLoader.registVideo('nimo.mp4')
    print(imgLoader.getThisFrame())


    