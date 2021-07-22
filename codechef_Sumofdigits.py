n = int(input())

for i in range(n):
    a = input()
    b = 0

    for x in a:
        b+= int(x)    
    print(b)    


    #another way is:
    #while (a>0):
    #    r = a%10
    #    sum += r
    #    a//=10
    #    print(sum)