from Rectangle import *
from Triangle import *
from Circle import *

def main():
    rect = RECTANGLE()
    tri = TRIANGLE()
    circle = CIRCLE()

    
    
    ##########################################
    while True:
        inputType = int(input("1. 직사각형, 2.삼각형, 3.원, 4. 종료\n"))
        if inputType == 4:
            break
        if inputType == 1 or inputType == 2:
            width,height = map(float,input("밑변 높이 입력 : ").split())
            if inputType == 1:
                rect.setWidth(width)
                rect.setHeight(height)
                rect.area()
                rect.showData()
            else:
                tri.setWidth(width)
                tri.setHeight(height)
                tri.area()
                tri.showData()
        else:
            radius = float(input("높이 입력 : "))
            circle.setRadius(radius)
            circle.area()
            circle.showData()

###################################

    # while True:
    #     inputType = int(input("1. 직사각형, 2.삼각형, 3.원, 4. 종료\n"))
    #     if inputType == 4:
    #         break
    #     saveData = {1:RECTANGLE(), 2:TRIANGLE(), 3:CIRCLE()}
    #     callClass = saveData[inputType]
    #     if 1 <= inputType <= 2:
    #         width,height = map(float,input("밑변 높이 입력 : ").split())
    #         callClass.setWidth(width)
    #         callClass.setHeight(height)
    #     else:
    #         radius = float(input("반지름 입력 : "))
    #         callClass.setRadius(radius)
    #     callClass.area()
    #     callClass.showData()
    
    
        
        


    
    

main()