import sys

def main():
    nInputTestCase = int(sys.stdin.readline())
    nMin = 0
    nMax = 0

    nTemp = list(map(int,sys.stdin.readline().split()))
    for i in range(0,nInputTestCase):
        if i == 0:
            nMin = nTemp[0]
            nMax = nTemp[0]
        else:
            if nMin > nTemp[i]:
                nMin = nTemp[i]
            elif nMax < nTemp[i]:
                nMax = nTemp[i]

    print(nMin,"",nMax)

main()