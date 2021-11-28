
import math

class SHAPE():
    def __init__(self) -> None:
        self._name = ""
        self._area = 0.0
        
    def showData(self):
        print("해당 도형의 타입은 {0:}이고, 넓이는 {1:.2f}입니다.".format(self._name,self._area))
    
    def area(self):
        pass