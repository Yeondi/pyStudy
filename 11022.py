
def main():
    t = int(input())

    for i in range(t):
        a,b = input().split()
        a= int(a)
        b=int(b)
        print("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))
        
main()