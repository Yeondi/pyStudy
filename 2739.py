
def main():
    n = int(input())
    
    for i in range(1,10):
        print(n,"*",i,"=",n*i)

    #위,아래 둘 다 맞음

    for i in range(1,10):
        print("{} * {} = {}".format(n,i,n*i))
main()