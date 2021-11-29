# Stack은 주로 이런식으로 구성이 되는데, 사실 list도 안쓰고 만들 수 있어.
# 단지 python이고, 초급반이기때문에 간단하게 list를 사용했어

class STACK():
    def __init__(self) -> None:
        self._saveData = [] # 일단 담을 공간을 마련해줘야지?

    def setSaveData(self,data):
        self._saveData.append(data)

    def getSaveData(self):
        return self._saveData

    def push(self,data): # 맨 뒤에 넣음
        self.setSaveData(data) # 리스트의 맨 뒤에 꽂힐 애야. 애초에 append라는애가 그런 역할

    def remove(self,data):
        self._saveData.remove(data)
        
        # 스택을 포함한 이러한 자료구조들의 기본 구성 3요소가 있어.
        # 1. 생성 / 2. 삭제 / 3. 검색
        # 여기서 사실 search라는 애를 만들어서 삭제와 생성이 가능하게 해야해.
        # 하지만 초급반이라 구성을 안했고  대신 remove라는 애를 만들어서 pop에서 쓸거야.
        # pop은 맨 끝 값을 삭제함과 동시에 값을 가져오는애인거 기억하지?
        
    def pop(self): # 맨 끝 값을 빼서 변수에 넣어주는애
        value = self.top() # 먼저 맨 위에 즉, 맨 뒤에 있는 애를 찾아서 임시로 저장하고 
        self.remove(value) # 앞서 만들은 애를 사용해서 삭제할거야.
        #self._saveData.pop() # 이것도 되는데 일부러 list의 요소를 사용 안한거야.
        return value # 그리고 얘는 값을 넘겨주는애라서 return이 필요

    def size(self): # 스택의 사이즈
        return len(self._saveData) # 사이즈는 len을 쓰면 돼

    def empty(self): # 비어있는지 / 안비어있는지 알려주는애
        if self.size() >= 1: # 앞서 만든 size를 사용해서 1 이상이면 무언가 있단 뜻이니까 안비어있다! 라는 뜻으로 False
            return False
        else: # 그게 아닌 경우는 0이니까 비어있다! 라는 뜻으로 True
            return True  # 함수 이름이 empty잖아 원래는 isEmpty()로 지어. = 이거 비었냐? 이거지

    def clear(self): # 전부 삭제하는애
        # for i in self._saveData:
            # self.remove(self._saveData(self.size()-1)) 
        self._saveData.clear()

        # 우선 첫번째 for문은 원래 이런식으로 만든다는걸 알려주려고 만든거야
        # saveData는 list니까 그걸 i에 담아서 우리가 만든 remove함수를 이용해서 하나하나 삭제할건데,
        # 문제는 data값이야. 근데 우린 끝에서부터 삭제하든 상관 없어 어쨋든 전부 삭제해야하니까
        # 이 경우는 for문에 range가 아닌 list값을 직접 꽂는식으로 선언해서 self._saveData에서 또 그 리스트 크기에서 -1번째 값을 가져와야해
        # 왜냐하면, 2개의 데이터가 있으면 index값은 0,1번이잖아? 그래서 하나를 빼야해
        # 엄청 번거롭지? 그래서 아래같이 짜면 좀 더 편해
        # for i in range(self.size()):
            # self.remove(self._saveData[i])
        # for문을 range를 써서 스택의 크기만큼 돌거야
        # 그리고 remove를 써서 삭제할건데 값이 필요하잖아? self._saveData에서 i번째 즉 처음엔 0번째 index의 값을 가져와서
        # remove에 꽂아서 삭제하란 소리야.

        # 물론 테스트는 귀찮아서 안해봤어  하고 에러나면 알려줄래?



    def top(self): # 맨 위에 있는 애 보여주는애
        dataSize = self.size()
        return self._saveData[dataSize-1]
        # 이미 말했던대로 맨 위에 있다 == 맨 뒤에있다이고,
        # 4개의 데이터가 있으면 0,1,2,3번지의 index가 존재하니, 데이터의 개수 -1을 해야 가장 뒤에있는 수가 리턴이 돼

    def show(self): # 저장된 값을 보여주는애
        for i in self._saveData: # self._saveData의 첫번째 값부터 하나씩 print해주는거야.
            print(i," ",end='')
        print()