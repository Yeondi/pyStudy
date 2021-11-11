import sys


# 얘도 c++에서 옮긴코드 기억이 가물가물하니 코드보면서 간략하게 설명하겠음
def main():
    nInputData = 0 #얘는 for문 안에서만 사용되는 애라서 이 구문이 없어도 상관무
    nCount = 0 # 얘는 무조건 여기. i의 for문 안에하면 맨 밑에 print(Count)를 못함

    arCompare = [0 for i in range(10)] # 이전문제에서 다룬것 미리 초기화하기

    for i in range(10):
        nInputData = int(sys.stdin.readline()) # 이젠 외울때 됐지?
        arCompare[i] = nInputData % 42 # 문제 그대로 받은 값의 42를 나눈 나머지를 list에 천천히 쌓아줄거야
        for j in range(i+1): # 별찍기문제랑 코드가 비슷하네? 어떤 원리인지 대략 감이 올거야.
            if arCompare[i] == arCompare[j] and i != j:
                # i가 0일때 , j는 0~1까지 한번 돌아가고, arComapre[0] == 1일거야. 예제처럼 1~10 들어간다는 가정을 할때
                # 그리고 i가 4라고 가정하자. 그럼 arCompare에는 1,2,3,4까지 막 들어갔을거야.
                # 그러면 4를 가지고 j는 다시 0이 된 상태니까 4랑 1 , 4랑 2, 4랑 3 이렇게 비교하고 4랑 4까지 비교하는건데
                # 같지 않은 경우를 찾는거니까 위 세번은 카운트를 쌓는데 4랑 4는 같잖아?
                # 근데 알고보니 나 자신이랑 나 자신이네? 그럼 그건 무효로 하는거야.
                # 하지만 만약 input이 42가 나온 후에 84가 나온 경우는 arCompare[i] == arCompare[j]더라도
                # 값이 같아도 번지수가 다르니 다른애잖아? 그런경우는 같은경우고 우린 다른경우만 찾는거니까 -1해주는거야
                # 그리고 이 이후는 검색하나마나 마찬가지라 break
                nCount-=1
                break
        nCount+=1 # 위 조건을 충족하지 않을경우는 무조건 다르다는 가정을 하는거야.
        # 위 코드를 짧게 말하면,
        # 수업 출석 부를때 본인 이름에 답하면 출석이고 아니면 다 결석으로 처리한다는 논리라고 보면 돼
    print(nCount)

main()