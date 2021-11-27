from character import C_CHARACTER

class C_MONSTER(C_CHARACTER):
    def __init__(self):
        super().__init__()

    def createCharacter(self,name="",gender="",uId=0,isSuper = False):
        self._name = self.shuffleName(2) # goblin ~ troll까지 섞기
        self.setHp(50)
        self.setAtk(5)
        super().createCharacter(name,gender,uId)
        return self

    def attack(self,monster):
        print()
        hit = self.getAtk() - monster.getDef()
        print("{0:}(이)가 {1:}에게 {2:}만큼 데미지를 주었다!".format(self.getName(),monster.getName(),hit))
        monster.setHp(monster.getHp() - hit)
        if monster.getHp() <= 0:
            monster.death()