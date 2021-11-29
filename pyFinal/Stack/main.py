from myStack import *

def main():
    stack = STACK()
    
    inputData = [0,0] 
    while True:
        inputData =input().split() # inputData에는 push,pop이런애들 nValue에는 숫자값들

        if inputData[0] == "push":
            stack.push(inputData[1])
            stack.show()
        elif inputData[0] == "pop":
            print(stack.pop())
        elif inputData[0] == "size":
            print(stack.size())
        elif inputData[0] == "empty":
            print(stack.empty())
        elif inputData[0] == "clear":
            stack.clear()
            print(stack.show())
        elif inputData[0] == "show":
            stack.show()
        elif inputData[0] == "top":
            print(stack.top())
        elif inputData[0] == "end":
            break
        else:
            print("명령어를 잘못 입력하셨습니다.")

main()