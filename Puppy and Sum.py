"""
a=int(input())
x_2 = 0
for i in range(a):
    x,y = map(int,input().split())
    x_3 = x*y
    for j in range(x_3):
        x_2 += x_3
        x_3-=1
    print(x_2)

"""
#below one is the correct one

t=int(input())
for i in range(t):
    k,n=map(int,input().split())
    for j in range(k):
        s=n*(n+1)//2
        n=s
    print(s)
