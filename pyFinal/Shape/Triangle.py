from Shape import *

class TRIANGLE(SHAPE):
    def __init__(self) -> None:
        super().__init__()
        self._name = "삼각형"
        self._width = 0
        self._height = 0
        
    def setWidth(self,width):
        self._width = width

    def setHeight(self,height):
        self._height= height

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def area(self):
        self._area = self._height * self._width / 2

    def showData(self):
        super().showData()
        print("그리고 삼각형의 넓이 공식은 밑변 * 높이 / 2 입니다.")