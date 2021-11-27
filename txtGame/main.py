from importList import *

def intro():
    print("")
    print("     A      TTTTTTTTTT  RRRRRRRR       EEEEEEEEE  EEEEEEEEE")
    print("    A A         TT      RR      RR     EE         EE")
    print("   A   A        TT      RR        R    EE         EE")
    print("  AA   AA       TT      RR      RR     EE         EE")
    print(" AAAAAAAAA      TT      RRRRRRRR       EEEEEEEE   EEEEEEEE")
    print(" AA     AA      TT      RR      R      EE         EE")
    print("AAA     AAA     TT      RR      RR     EE         EE")
    print("AA       AA     TT      RR        RR   EEEEEEEEE  EEEEEEEEE")
    print("#############################################################")
    print("#############################################################")

def initGame(c,uId):
    
    name = input("이름을 입력해주세요 : ")
    gender = input("성별을 입력해주세요 : 예) '남' '여' ")

    c.createCharacter(name,gender,uId)

def lstCharacters(lst):
    for i in range(len(lst)):
        print("{0:}. {1:}.".format(i+1,lst[i].getName()))
        
    data = int(input("캐릭터 선택 : ")) - 1
    return lst[data]

def gameStart(uId):
    numOfEnemy = random.randrange(1,4)
    cm = list()
    
    for i in range(numOfEnemy):
        c = C_MONSTER()
        cm.append(c.createCharacter(c))
    
    print()
    for i in range(numOfEnemy):
        print("몬스터 {0:}(이)가 출현했다!".format(cm[i].getName()))
        battleStart(uId,cm[i])

def battleStart(user,monster):
    print("1. 공격하기")
    selectOne = int(input("2. 도망가기\n"))
    if selectOne == 2:
        if monster.getIsRunAway():
            print("성공적으로 도망쳤다!")
            return True
        elif not monster.getIsRunAway():
            print("보스몬스터를 상대로 도망을 갈 수 없어!")
            user.attack(monster)
    elif selectOne == 1:
        user.attack(monster)
        monster.attack(user)
    
    

def main():
    intro()
    print("1. 게임시작")
    start = int(input("0. 종료하기\n"))
    uId = 0
    count = 0
    playableCharacters = list()

    if start == 0:
        print("아니, 진짜 종료하려구요? 어차피 친구도 없잖아요 한번 더 기회드릴께요")
        isReal = int(input("0. 그래도 종료하기\n"))
        if isReal == 0:
            sys.exit()
    while True:
        print()
        print("1. 캐릭터 생성하기")
        selectMenu = int(input("2. 캐릭터 선택하기\n"))
        if selectMenu == 1:
            c = C_USER()
            uId = random.randrange(0,2000000000)
            count += 1
            initGame(c,uId)
            print("생성된 캐릭터의 정보는 다음과 같습니다.")
            print()
            c.showData()
            playableCharacters.append(c)
        elif selectMenu == 2:
            if count <= 0 :
                print("캐릭터가 존재하지 않습니다.")
                continue
            print()
            print("고르실 캐릭터를 선택해주세요\n")
            selectCharacter = lstCharacters(playableCharacters)
            gameStart(selectCharacter)
            

            
        
        



main()