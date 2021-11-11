import sys


def calcRest(nNum, nData): # tot값 , 나눌 자리수 값 (십의자리면 10,백의자리면 100)
	nNum %= nData # 이건 직접 디버깅을 해보거나 가상의 수를 대입해서 풀어보면 뭔소린지 알거야
	nData /= 10
	nNum /= nData

	return int(nNum)

# 이건 C++코드여서 변환과정에서 코드를 거의 일부만 수정해서 알아보기 힘드므로 주석으로 설명을 할건데
# 이해 못해도 그런갑다하고 물어보면 됨!
def main():
    nInputData1 = int(sys.stdin.readline())
    nInputData2 = int(sys.stdin.readline())
    nInputData3 = int(sys.stdin.readline())
    # 리스트 3개 선언해서 받아도 무방

    tot = nInputData1 * nInputData2 * nInputData3 # 일단 총 값 구하기

    arResult = [0 for _ in range(10)] # 이게 c++의 잔재인데
    # 우리는 보통 arResult = []이렇게 선언을 하는데 c++은 기본은 데이터 크기를 알려줘야해
    # 그래서 0~9의 개수를 채울 배열을 선언할때 그냥 int atResult[10]; 이런식으로 선언해도 되는데
    # 파이썬은 기본이 [] 이런식으로 크기가 정해지지않은 리스트라서 arResult[1]이런식으로 접근하면 무조건 에러남
    # 그래서 일부러 코드 고치기 싫어서 0으로 전부 초기화한거야
    # [0 for _ in range(10)] == _의 변수의 시작은 0이고 10까지 작동을 하는데 0으로 값을 다 채워버리겠다는 뜻
    # 그래서 [0,0,0,0,0,0,0,0,0,0] 이렇게 초기화됨. 모르면 print(arResult) 해볼것
    nCount = 0 # 말 그대로 값 카운트 해주는애
    nBaseData = 10 # 얘는 tot값이 17037000 뭐 이런식으로 나오면, n의 자리로 끊어줘야해서 뒤에서 부터 끊어주려고
    # 10을 준건데, 이건 반대로 c++의 단점이야. python은 len으로 길이를 재서 길이만큼 10 * 길이 해줘서 총 길이값을 구하고
    # 앞에서부터 잘라주면 엄청 쉽거든  이게 c++이 오래된 언어라는 증거지.

    arFinalResult = [0 for i in range(10)] # 진짜 결과 값을 가지고 있는애
    # 종종 Result라고 이미 지었을경우 이렇게 지음 ㅋㅋ 찐막, 찐찐막 , 찐찐찐막 이런거 알지?
    while tot>0: # tot값이 존재할경우 단위별로 잘라서 카운트하는애
        tot/=10
        tot = int(tot)
        nCount+=1

    tot = nInputData1 * nInputData2 * nInputData3
    # 이건 내가 옛날에 푼거라 구식코딩인데, 위에 while문에서 tot값을 10으로 나눴는데
    # 굳이 안그래도 돼. 그냥 nTemp = tot 라고 만들어서 nTemp에 복사해서 그 값을 가지고 놀면 됨
    # 그러면 이 tot 계산을 반복 안해도 돼

    for i in range(nCount): 
        arResult[i] = calcRest(tot,nBaseData) 
        # 여기까지 원리를 간단하게 말하면, 위 while tot>0: 문에서 10씩 계속 나눠서 총 자리수를 구하는거야.
        # python은 자료형을 지 맘대로 바꿔서 tot에 계속 int로 캐스팅 해줘야해 아니면 0.17 이런식으로 값이 미친듯이 들어가.
        # 예제에 답이 17037300인데, 천천히 돌려보면 알겠지만 일의자리부터 하나씩 개수를 세서 카운트하는게 보일거야.
        # 0->0->3->7->3->0->7->1 이런식
        nBaseData *=10

    for i in range(nCount):
        #여긴 코드가 아예 다르게 바뀜
        #기존에는 switch / case라는 구문을 사용해 풀었는데
        #python엔 그게 없기때문에 if-elif-else로 처리할거야
        #switch (arResult[i]) 이 안에 값이 0이면 0번지에 값 추가
        arFinalResult[arResult[i]] += 1
    for i in range(10):
        print(arFinalResult[i])

    #arResult는 input에 들어간 세개의 값을 합을 자리수별로 나누어 집어넣은것
    #arFinalResult는 0~9까지 개수를 세어 넣는곳
    #arFinalResult[0]은 0의 개수가 들어있는곳
    #[1]은 1의 개수가 들어있는곳이야. 이해가지? 모르겠으면 직접 써봐!
main()