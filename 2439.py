
def main():
    nInput = int(input())

    for i in range(nInput):
        for j in range(nInput-i-1,0,-1): #이건 모르면 물어볼것. 말하면서 풀어줘야함
            print(' ',end='')
        for k in range(i+1):
            print('*',end='')
        print()



main()