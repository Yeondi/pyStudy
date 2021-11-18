# 1. 변수 타입 확인하기
a = 5
b = 3.4
c = "asd"
d = True
print(type(a))  # type함수 사용하기

# 입력
# input
a = input("a값 입력 : ")
# 여러개를 입력받을경우
x,y = input("x y값 입력 : ").split() # input은 기본타입이 String
x = int(x)
y = int(y) # 그래서 int형으로 써야할경우 캐스팅 해줌 

print("a1,b1입력 : ",end='')
a1,b1 = map(int,input().split()) # 이건 int로 캐스팅하면서 여러개 입력받게 해주는애
# map함수인데 외워두면 굉장히 좋음

# 출력의 두가지
# print
print("a1의 값은 : " + str(a1)) # a1을 입력할때 map을 이용해서 int로 캐스팅 할 경우 문자열끼리 합쳐주는 + 연산자가 안되므로
# str형으로 캐스팅할것

#format
print("a1의 값은 {0:}".format(a1))

#이렇게 보면 format이 굉장히 비효율적으로 보이지만
#들어가는 변수의 타입이 int int float 이런 경우면
print("a1의 값은 : " , a1 , "b1의 값은 : " , b1 , "나눈값은 : ",a1/b1,"이다.") # 이 방식은 + 연산자가 아닌 comma를 사용했기때문에
# 따로 캐스팅을 안해도 된다.

print("a1의 값은 {0:}이고, b1의 값은 : {1:}이고, 나눈값은 : {2:.2f}이다.".format(a1,b1,a1/b1))

# 위 두개의 차이를 보면 첫번째는 문자열의 시작과 끝 그리고 + 오퍼레이터를 반복적으로 해야하는 번거로움이 있지만
# format의 경우 한꺼번에 입력하고 한꺼번에 변수를 주면 된다.
# 위 format함수는 {0:} 이건 기본타입으로 뒤에 format()하고 첫번째 변수가 올 자리라는 뜻
# {1:} 역시 두번째 변수가 올 자리이며, {2:.2f}는 3번째 변수를 소수 둘째자리까지 표시한다는 뜻이다.

# if는 너무 쉬우니 패스

# for문은 별 찍어보기
inputNumber = int(input())
for i in range(inputNumber):
    for j in range(0,i+1):
        print("*",end='')
    print()

# 위 별찍기 코드를 말로 풀어보자면, inputNumber에 input()함수로 문자열을 받아와서 그것을 정수형으로 캐스팅을 하고 그것을 inputNumber에 넣는다.
# inputNumber가 5라면, i는 0~5, j는 i+1까지 돌아야한다.
# 왜 i+1이냐? i값은 0에서 시작하기때문에 i+1로 안해주면 1 2 3 4 이렇게 찍힌다.
# 반대로 i를 1부터 시작하고 j의 for문에서 i+1이 아닌 i로 해줘도 된다.
# end=''의 기본형은 end='\n' 으로 \n은 Enter효과를 낸다는것. 근데 우린 거길 공백으로 대체하겠단 뜻으로
# 한마디로 별을찍고 한줄을 안띄겠다.라는 뜻
# 그 밑 print() 이것은 이 자체만으로도 아무것도 출력을 안하고 한줄을 넘겨버려서 이렇게 둔것

#inputNumber재사용
while True: # 참인동안 돌아라
    if inputNumber < 0 : # inputNumber가 0보다 작으면 break해라
        break
    inputNumber-=1 # inputNumber를 1씩 깎는다.

while True:
    if inputNumber % 2 == 0: # inputNumber를 2로 나눴을때 나머지가 0이면, 즉 짝수이면 continue
        continue # 얘는 밑에 if inputNumber > 10:부터 while문의 맨 밑까지 아예 안읽고 while문 상단으로 바로 간다.
    if inputNumber > 10:
        break
    print(inputNumber) # 여기서 찍어보면 짝수는 안나온다.
    inputNumber+=1

#리스트
lst = []
lst1 = list() # 선언은 둘 다 가능
lst2 = [1,2,3,[4,5,6]] # 2차원
lst1.append(1) # 1의 값이 추가됨
lst1.append(2)
lst1.append(3)
lst1.append(4)
lst1.append(5)
a = lst1.pop(1) # 1번째 인덱스인 2가 lst1에서 빠지고 그 값이 a로 들어감
print("pop한 a의 값 : {}".format(a))

#나머지는 생략
tup = tuple()
# list처럼 tuple에 .을 찍어 함수들을 호출하려해도 append라던가 remove등 수정가능한 함수가 없다.
tup = list(tup) # 이렇게 list로 캐스팅한 후 값을 바꿔주면 된다.

dic = {'이름':'유경민','나이':27,'이름':'서지현'}
#이렇게 할 경우 {이름:서지현,나이:27} 이렇게, 키가 중복될경우 나중에 온 키 값이 기존의 키 값을 대체한다.
print(dic.keys())
print(dic.items())

lst5 = list(dic.keys())

#함수
def func():
    print("이것은 함수입니다.")

print(func) # 참고로 모든 언어는 위에서 아래로 읽어서 이 경우 print를 def func보다 위에 올리면 에러가 날 수도 있다.
# c++의 경우는 나는데 python은 딱히 안해봄

# 따라해보기
# add함수를 만들테니 , sub,mul,div  뺄셈,곱셈,나누기를 구현해보자.
def add(nData1,nData2):
    return nData1+nData2

#sub

#mul

#div

# def printFunc(nData):   # 매개변수 자유 (괄호안에 들어오는게 매개변수), return 사용없이 print사용해서 값 알려주기

# 여기서부턴 다른 파일이라고 생각할것
# 예로들어 여기가 파일의 첫줄이다?

# 난 아래와 같이 쓰는데, 우선 코드를 보면, 함수 이름을 main이라 정의했고 밑엔 main을 호출했다.
# 컴퓨터는 가장 바깥개념에 있는애를 먼저 읽기때문에, 함수보다 밑에 있더라도 함수 바깥에 있는 main()을 호출하고
# 우린 main을 기존에 쓰던것처럼 사용하면 되는데, 왜 이런걸 사용하냐면
# 프로그래밍을 하면서 함수,클래스를 추가할때가 생기는데 main의 영역을 지정해주지 않으면 코드가 난잡해진다.
# 한마디로 예쁘게 정리하려고 main코드를 묶어버린것.


# def main():

# main()







