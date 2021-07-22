t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    d = [a,b,c]
    e = max(d)
    d.remove(e)
    print(max(d))