from myStack import *

def main():
    stack = STACK()
    
    inputData = [0,0] 
    while True:
        inputData =input().split() # inputData에는 push,pop이런애들 nValue에는 숫자값들

        # 구별을 잘 해야해 일단 top,empty,size는 return값이 존재해
        # 때문에 무조건 print구문을 사용해 보여줘야하고
        # 다른애들은 그냥 show로 보여주면 되는거야

        # 위에 inputData는 a,b = map(str,input().split()) 이렇게도 가능한데,
        # 대신 pop 이렇게만 입력하면 에러가 나
        # 그래서 일부러 두칸짜리 리스트를 만들어주고 그곳에 값을 넣은건데
        # 내가 이미 두칸짜리를 만들었기때문에, 두번째로 값이 입력이 되던 말던 상관없어
        # push 10 이라고 입력될꺼니까 push는 명령어고 10은 값이여야해
        # 이걸 생각해서 밑에 코드를 참고해

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