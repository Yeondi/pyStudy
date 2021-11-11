import sys

def main():
    t = int(input())

    for i in range(t):
        a,b = input().split() #한번에 int(input().split()) 하면 오류남
        a = int(a) # 그래서 이렇게 따로 캐스팅한걸 그대로 넣어줌
        b = int(b)
        print(a+b)

main()