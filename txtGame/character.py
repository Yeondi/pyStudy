from enum import Enum
import random
import sys

class E_RANDOM_MONSTER_NAME(Enum):
    goblin = 1
    bat = 2
    Brenda = 3
    troll = 4
    jamesRyu = 5
    JaeHeeAhn = 6      # 영문명 달라도 이해좀 ㅎㅎ.
    SungjinKim = 7
    UijinCho = 8       # 조씨는 Cho, jo 둘로 갈리길래

class C_CHARACTER():
    def __init__(self):
        self._name = "" # 이름
        self._atk = 5 # 공격력
        self._def = 1 # 방어력
        self._hp = 100 # 체력
        self._mp = 50 # 마나
        self._callEnum = E_RANDOM_MONSTER_NAME
        self._id = 1
        self._runAway = True # 도망을 칠수있는가?

    def setName(self,name):
        self._name = name
    def setAtk(self,atk):
        self._atk = atk
    def setDef(self,defence):
        self._def = defence # 그냥 def는 예약어 def가 있음 그래서 안됨
    def setHp(self,hp):
        self._hp = hp
    def setMp(self,mp):
        self._mp = mp
    def setId(self,id):
        self._id = id

    def getName(self):
        return self._name
    def getAtk(self):
        return self._atk
    def getDef(self):
        return self._def
    def getHp(self):
        return self._hp
    def getMp(self):
        return self._mp
    def getId(self):
        return self._id
    def getIsRunAway(self):
        return self._runAway()
    
    def createCharacter(self,name="",gender="",uId=0,isSuper = False):
        if isSuper:
            self._name = "GM " + self._name
            self._atk = 999999999
            self._def = 999999999
            self._hp = 999999999                           # 함수 내부에선 바로 꽂아줘도 되긴함
            self._mp = 999999999                           # 여러가지 예를 보여주려고 이렇게 했음
            print("운영자의 슈퍼캐릭터 생성 완료")
        self._id = id

    def shuffleName(self,ctype):
        if ctype == 2:
            randValue = random.randrange(1,5)
        elif ctype == 3:
            randValue = random.randrange(5,9)
        for i in range(4):
            if randValue == self._callEnum.goblin.value:
                return "고블린"
            elif randValue == self._callEnum.bat.value:
                return "코시국 그녀석"
            elif randValue == self._callEnum.Brenda.value:
                return "캐나다 노숙썰 만들어준 사람"
            elif randValue == self._callEnum.troll.value:
                return "내친구 별명 트롤임"
        return ""

    def death(self):
        print("{0:}(이)가 죽었습니다.".format(self._name))
            
    def showData(self):
        print()
        print("데이터 검색결과 : ")
        print("닉네임 : {0:},\n공격력 : {1:},\n방어력 : {2:},\n체력 : {3:},\n마나 : {4:}".format(self.getName(),self.getAtk()
                        ,self.getDef(),self.getHp(),self.getMp()))
        print("ID : {0:}".format(self.getId()))
    
    def attack(self,monster):
        pass

    