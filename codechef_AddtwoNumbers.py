t = int(input())


for i in  range(t):                          #range is given in t
    a = sum(map(int,input().split()))        #this adds your splitted distinct inputs together(integers)
    print(a)