def funOne(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
    print()
    
def funTwo(n):
    for i in range(1,n+1):
        if(i*i>n):
            break
        if(n%i==0):
            print(i,int(n/i),end=" ")
    print()

n = int(input())
funOne(n)
funTwo(n)
