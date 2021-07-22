n = int(input())
y = []
count_1 = 0
count_2 = 0
for i in range(n):
    x = int(input())
    y.append(x)
    
y.sort()
if len(y)%2==0:
    z = len(y)//2
    for j in range(z+1):
        count_1= len(y[z-1:])
    print(count_1*y[z-1])    
elif len(y)%2!=0:
    z = int(len(y)//2)
    for a in range(z+1):
        count_2 = len(y[z:])
    print(count_2*y[z]) 
else:
    print("ERROR")    