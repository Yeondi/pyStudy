from character import *

class C_USER(C_CHARACTER):
    def __init__(self):
        super().__init__()
        # C_CHARACTER().__init__() # 위 아래 둘 다 가능
        self._gender = ""
        self._cash = 5000
    
    def setGender(self,gender):
        self._gender = gender
    def setCash(self,cash):
        self._cash = cash

    def getGender(self):
        return self._gender
    def getCash(self):
        return self._cash

    def createCharacter(self,name="",gender="",uId=0,isSuper = False):
        C_CHARACTER().createCharacter(name,gender,uId)
        self.setName(name)
        self.setGender(gender)
        self.setId(uId)
        self.setAtk(10)
        print("{0:} 유저캐릭터 생성 완료".format(self.getName()))

    def showData(self):
        super().showData()
        print("소지한 돈 : {0}".format(self.getCash()))
    
    def death(self):
        super().death()
        sys.exit()

    def attack(self,monster):
        print()
        hit = self.getAtk() - monster.getDef()
        print("{0:}(이)가 {1:}에게 {2:}만큼 데미지를 주었다!".format(self.getName(),monster.getName(),hit))
        monster.setHp(monster.getHp() - hit)
        if monster.getHp() <= 0:
            monster.death()