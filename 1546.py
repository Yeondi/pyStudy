import sys

#이것도 c++코드 옮긴것
def main():
    nInputObject = int(sys.stdin.readline()) # 일단 몇개를 받을지
    arScore = [0 for i in range(1000)] #최대 1000보다 작거나 같다.
    nMax = 0 # 얜 두개의 각기 다른 for문에 쓰이기에 여기가 맞음
    fResult = 0.0 # 얘도 같음

    arObjectScore = list(map(float,sys.stdin.readline().split())) # list에 값을 한번에 꽂을때 이렇게 해야함. 일단 외우기
    # 40 60 80이 들어왔다고 가정
    for i in range(nInputObject):
        if i == 0: # 맨 처음만 이렇게. 반복문 바깥에서 nMax = arObjectScore[0] 이렇게 해도 됨. nMax에 어쨋든 값이 있어야해서 이런거
            nMax = arObjectScore[i]
        if i != 0 and nMax < arObjectScore[i]: # 맨 처음이 아니면서 최대값보다 arObjectScore의 현재값이 더 큰경우
            nMax = arObjectScore[i] # 최대값을 바꿔주고

    for i in range(nInputObject):
        #예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
        #문제에 나온 그대로 값을 계산해주면 됨
        #위에 for문이랑 분리한 이유는 값을 받으면서 계산하지 않기위해
        arScore[i] = arObjectScore[i] / float(nMax) * 100.0 

    for i in range(nInputObject):
        fResult += arScore[i] # arScore에 세준이의 계산 방식의 결과가 들어있는걸 fResult에 일단 값을 쌓아줄거야.
        if i == nInputObject -1: # 3개의 값을 입력 받았을경우 nInputObject는 3이 나올수도 있는데, 안전을 위해
                                # -1까지 연산해준건데, 없어도 될거같네 c++에선 다르게 계산했었는데 그 잔재야
            fResult /= float(nInputObject) # 각 값을 쌓아줬으니 그걸 n으로 나눠줘야지? 그냥 그 과정이야.

    print(fResult) # 그리고 그게 정답이지

main()