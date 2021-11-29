
class STACK():
    def __init__(self) -> None:
        self._saveData = []

    def setSaveData(self,data):
        self._saveData.append(data)

    def getSaveData(self):
        return self._saveData

    def push(self,data): # 맨 뒤에 넣음
        self.setSaveData(data)

    def remove(self,data):
        self._saveData.remove(data)
        
    def pop(self): # 맨 끝 값을 빼서 변수에 넣어주는애
        value = self.top()
        self._saveData.pop()
        return value

    def size(self): # 스택의 사이즈
        return len(self._saveData)

    def empty(self): # 비어있는지 / 안비어있는지 알려주는애
        if self.size() >= 1:
            return False
        else:
            return True

    def clear(self): # 전부 삭제하는애
        self._saveData.clear()

    def top(self): # 맨 위에 있는 애 보여주는애
        dataSize = self.size()
        return self._saveData[dataSize-1]

    def show(self): # 저장된 값을 보여주는애
        for i in self._saveData:
            print(i," ",end='')
        print()