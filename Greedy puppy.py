for i in range(int(input())):
    N,K = map(int,input().split())
    if N%2!=0:
        print(int(N-(K*K)))
# the above one didn't work out as expected
#the below one got accepted
try:
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        l=0
        for j in range(1,b+1):
            l=max(a%j,l)
        print(l)
except:
    pass