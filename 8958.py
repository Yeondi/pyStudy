import sys

def main():
    nInputTestCase = int(sys.stdin.readline())
    for i in range(nInputTestCase): # n번 실행하는거니까
        ox = list(map(str,sys.stdin.readline().split())) 
        # 해석 : ox는 입력을 받은(sys~readline()까지)문자열을 split을 해서 str로 캐스팅 한 다음에 list로 캐스팅을 해서 넣어라
        score = 0 # 점수를 저장할 애
        combo = 0 # 콤보를 쌓을 변수
        for j in range(len(ox[0])): # 이건 반대로 파이썬의 안좋은 점이야.
            # c++계열의 경우 str이라는 애 자체가 배열이라 그냥 쓰면 되는데 여긴 꽂기도 귀찮고
            # 대충 꽂으면 ox의 리스트 안에 박혀버려
            # 물론 더 좋은 방법이 있지만 쉬운문제라 pass
            # 디버깅 해보면 알겠지만 ox[0]에 'oxooxooxox'이러한 입력했던 문자열이 들어있을거고
            # string은 사실 배열이랬지? ox[0][0] 이렇게하면 str값에서 맨 첫번째가 나오는 방식이고 [0][1]이면 다음 값이 나와
            # 직접 하나하나 실행해봐
            if ox[0][j] == 'O': # O일경우
                score += 1 + combo # 위에 combo = 0으로 해놓은 이유야. 맨 처음은 combo가 0이어야하고
                combo+=1 # 콤보점수를 쌓아주기. 만약 이 OXO 이렇게면 한번은 X 즉 틀렸단거고
                        # 틀린건 combo점수가 날라간다는것. 그래서 아레 else엔 0으로 다시 값을 준거야
            else: combo = 0 # 어차피 연속으로 O면 이 else는 거치는 일이 없으니까
        print(score)

main()