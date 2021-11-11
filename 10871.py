import sys

def main():
    n,x = input().split()
    n,x = int(n),int(x)

    lst = list(map(int,sys.stdin.readline().split()))
    
    for i in range(n):
        if lst[i] < x:
            print(lst[i],end=' ')
main()