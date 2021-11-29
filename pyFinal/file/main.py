# member.txt파일 생성 후 입력까지 마친 상태

def main():
    inFile = open('./file/member.txt').readlines() # inFile이란 변수를 만들어서 open을 하겠다 ' ' 안에 있는 주소를 그리고
    for i in inFile:                               # 라인을 전부 읽겠다.
        print(i)                                   # 이건 설명이 길어서 글로 쓸게
    outFile = open('./file/member.txt','w')         # 아까와 조금 다르지? 'w'가 붙었어. 사실 저 위에는 'r'이라는 애가 붙어있어
    outFile.write('재밌었어 얘들아 ! \n')           # r은 read 즉 읽기형식으로 열겠다. w는 write 즉 쓰기형식으로 열겠다.
    for i in inFile:                                # 불러온 파일을 변수에 넣고 .write(내용) 하면 해당 내용이 넣어지는데
        outFile.write(i)                            # 만약 여기 옆에 for문이 없으면 기존에 있던 내용은 전부 지워지고
main()                                              # 재밌었어 얘들아! 만 입력돼