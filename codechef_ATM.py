x,y = input().split()
x = int(x)
y = float(y)

if x <= y :
    if x%5==0 :
        z = y-x
        a = (z-0.5)
        print(a)

    else :
        print(y)    

else :
    print(y)        