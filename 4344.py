import sys

# 얘도 c++옮겨온것
def main():
    # 이건 문제를 잘 읽어야해. 입력을 보면 5 한줄띄고 5 50 50 70 80 100 이렇게 있지?
    # 첫줄에 혼자 있는 n은 n번 입력해야한다는 뜻이고
    # 둘째줄에 첫번째숫자 m은 m개의 과목의 점수를 입력해야 한다는 뜻이야.
    # 그래서 50 50 70 80 100 이게 총 과목의 수야.
    n = int(sys.stdin.readline())
    for i in range(n):
        nSum,nCount,avg = 0,0,0.0
        arObjScore = list(map(int,sys.stdin.readline().split())) # 이건 몇번봐서 낯이 익으니 외우고 이해할것
                                                                # 이해안되면 말해 더 쉽게 알려줄게
        nNum = int(arObjScore.pop(0)) # pop배웠지? pop(n)은 n번째 인덱스 값을 pop한다는 뜻으로 nNum에 값을 넣어줄거야.
                                    #이러면 따로 remove하거나 인덱스를 안걸러도 돼

        for j in range(nNum): # 과목의 수
            nSum += arObjScore[j] # nSum이라는 애한테 각 과목의 점수를 쌓아줄거야 우리가 쓰던 tot랑 같아
        
        avg = nSum / nNum # 총 점수 : nSum / 과목의 수 : nNum 이해되지?
        
        for k in range(nNum): # 과목의 수
            if avg < arObjScore[k]: # 과목의 점수와 평균을 하나하나 비교하기 위한거야. 
                nCount+=1 # 과목의 점수(예로 90)이 평균(예로 50)보다 높잖아? 그러면 nCount에 1이 쌓이는거지
                # nCount는 과목의 점수가 평균보다 높은 개수를 저장하는 변수

        # 여기서 부턴 두가지 방법이 있어        format사용 혹은 round사용
        fData = float(nCount/nNum*100)
        strResult = "{0:0.3f}%".format(fData) #1번방법 
        # format함수는 문자열 뒤에 붙일수 있는 함수야.
        # "유경민".format() 이것도 가능해
        # 아무튼 "{0:0.3f}%".format(fData) 이 뜻은 {}은 format의 값이 들어오는 자리라는 뜻이고
        # 0: 은 0번째 인덱스 즉 format함수에서 첫번째로 입력된 변수가 다음과 같이 적용된다는 뜻이야.
        # 0.3f는 float형을 3번째소수점까지 무조건 표시해주는 애
        # TMI로 번호를 부여할때 1~100을 이쁘게 하려면 010 011 012 이렇게 해줘야 하잖아?
        # 그럴땐 03d하면 강제로 3자리로 만들어줘
        # 암튼 그런 후 }를 닫고 %문자열을 보여준다는 뜻이야.
        print(strResult)

        # 아래 방법은 round라는애를 사용하는건데 얘는 '강제'가 없어.
        # 무슨말이냐면 50.000%가 나오면 50.0%로 표기해버려
        # 그래서 해당 문제엔 적용이 안되지만 이런 룰만 없으면 얘도 사용가능해
        
        # print(round(float(nCount/nNum*100),3)) #2번방법
        # 무엇이든 뜯어볼때 print를 먼저 읽고 round읽고 float읽어서
        # 가장 안쪽으로 들어가면 nCount / nNum * 100있잖아?
        # 이걸 먼저 본 후에 계산을 한 값을 float로 캐스팅 하라는거고
        # float를 직접 감싼애는 round지?
        # round(값,자리수) 얘는 반올림 해주는애야. 
        # 값을 대상으로 소수점 이하 n개의 자리수만큼 표현한다는 애야
        # 그래서 0하면 소수점이 안나올거야 아마도? 
        # 문제를 읽어보면 소수점 셋째자리'까지' 표현하라 했으니 3이라 적어준거고

main()