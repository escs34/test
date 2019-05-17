from abc import *

class Oracle(metaclass=ABCMeta):
    @abstractmethod
    def predict(self, image):
        print("There's nothing i can do with this.")

    @abstractmethod
    def predict_and_drow(self, image):
        print("This method is made for test")