x = int(input())
y = 0
z = 0
s = 0

for i in range(x):
    n = int(input())
    ld = n % 10
    while n > 0:
        r = n % 10
        y = y * 10 + r
        n = int(n / 10)
        

    z = y % 10
    s = z + ld
    print(s)    

