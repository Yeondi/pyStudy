from Shape import *

class CIRCLE(SHAPE):
    def __init__(self) -> None:
        super().__init__()
        self._name = "원"
        self._radius = 0

    def setRadius(self,radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

    def area(self):
        self._area = math.pow(self._radius,2) * math.pi

    def showData(self):
        super().showData()
        print("그리고 원의 넓이 공식은 반지름 * 반지름 * pi 입니다.")