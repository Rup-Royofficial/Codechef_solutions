t = int(input())
for i in range(t):
    a,b  = map(int,input().split())
    if a>b:
        print(">")
    if a<b:
        print("<") 
    if a==b:
        print("=")       