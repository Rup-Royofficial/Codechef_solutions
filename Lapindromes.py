n = int(input())
count = 0
for i in range(n):
    x = input()
    for j in x:
        z = len(x)
        if z%2==0:
            x_1 = x[:z//2]
            x_2 = x[z//2:]
            
            if (x_1==x_2 or x_1==x_2[::-1]) :
                print("YES")
                break
            else:
                print("NO")
                break    
            
        if  z%2!=0:
            x_1 = x[:((z//2))]
            x_2 = x[((z//2)+1):] #((z//2)+1):]
            if (x_1==x_2 or x_1==x_2[::-1]):
                print("YES")
                break
            else:
                print("NO")
                break    
                   
"""
t=int(input())
for i in range(t):
    n=input()
    l=len(n)
    l1=[]
    l2=[]
    mid=l//2
    for i in range(0,mid):
        l1.append(n[i])
    if(l%2==0):
        for j in range(mid,l):
            l2.append(n[j])
    else:
        for j in range(mid+1,l):
            l2.append(n[j])
    l1.sort()
    l2.sort()
    if(l1==l2):
        print("YES")
    else:
        print("NO")
"""        