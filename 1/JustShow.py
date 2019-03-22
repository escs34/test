from Sender import Sender

class JustShow:
    def __init__(self):
        self.sender = Sender()

    def showMenu(self):
        selectNumber = -1
        while True:
            print()
            print()
            print()
            print("...................................................................")
            print("Choose Menu")
            print("...................................................................")
            print("1. input the video")
            print("2. show next first image")
            print("...................................................................")
            selectNumber = int(input("Input Menu Number. "))

            if selectNumber == 0:
                break
            elif selectNumber == 1:
                self.inputVideo()
            elif selectNumber == 2:
                self.showNext1()
            elif selectNumber == 3:
                self.showNext100()
            elif selectNumber == 4:
                self.showNext1000()

    def inputVideo(self):
        path = str(input("input video's path. "))
        self.sender.registVideo(path)

    def showNext1(self):
        self.sender.getThisFrame()
        print("i got 1 frame")

    def showNext100(self):
        pass

    def showNext1000(self):
        pass

