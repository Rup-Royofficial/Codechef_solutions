 
n = int(input())
for i in range(n):
    cnt = 0
    x = int(input())
    y = list(map(int,input().split()))
    
    for j in y:
        if j>=max(y) and len(y)>=1:
            cnt+=1
            y.remove(j)
    print(cnt)
            