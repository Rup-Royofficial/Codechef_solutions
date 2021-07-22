n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a>= 1000:
        x = (a*b)-((a*b)*0.1)
        print(x)
    else:
        print(a*b)
