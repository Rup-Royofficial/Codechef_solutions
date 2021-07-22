n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    z = x+y
    z_1 = z-x
    z_2 = z-y
    if z_1>z_2:
        print(f"{z_1} {z}")
    else:
        print(f"{z_2} {z}")