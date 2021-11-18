# 텍스트형 게임 만들기

class C_CHARACTER():
    # 코드 작성 #
    hp = 5
    mp = 5
    name = ""
    atk = 5
    defence = 3
    def setData(self,name):
        self._name = name
    pass

def fight(hero1,hero2):
    # 체력 = 체력 - (공격력-방어력)
    print("{0:}가 {1:}를 공격했다 !")
    # input your code
    # switch side
    print("{0:}가 {1:}를 공격했다 !")

    # if hero1 or hero2의 체력이 0 이하일경우 ???가 죽었습니다 메세지와 함께 게임 종료 시그널 보내기
    print("{0:}의 체력은 {1:}이고, {2:}의 체력은 {3:}이다.")
    
    return ###

def main():
    while True:
        nInputNumber = input("1. 게임 시작하기 \n 0. 게임 종료하기")
        if nInputNumber == 0:
            break
        # 캐릭터에게 닉네임(name) , 체력(hp), 마력(mp), 공격력(atk), 방어력(defe)를 할당하기.
        # 해당 정보가 저장되어야함.
        
        # 두 캐릭터를 만들어서 저장하기.
        countCharacter = 1
        print("캐릭터{}의 닉네임을 설정해주세요! : ".format(countCharacter),end='') #
        name = input() 
        hero1 = C_CHARACTER()
        #code
        hero2 = C_CHARACTER()
        #code

        # print(hero1,hero2) # 확인하기 

        #만일 위를 마쳤다면, 둘이 싸우게 해보기
        fight(hero1,hero2)

        # 누가 죽었다면, 게임종료

        # 이번만 코드를 바꾸기 허용함!
        # 대신 다음부턴 주어진 skeleton코드에 자신의 코드만 더해서 할것
    


main()