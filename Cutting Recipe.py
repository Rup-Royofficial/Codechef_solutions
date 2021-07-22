def hcf(n1, n2):
    while (n1 != n2):
        if (n1 > n2):
            n1 = n1 - n2
        else:
            n2 = n2 - n1

    return n1


t = int(input())
while t > 0:
    l1 = []
    l = list(map(int, input().split()))
    h = l[1]
    for i in range(2, len(l)):
        h = hcf(h, l[i])
    for i in range(1, len(l)):
        print(l[i] // h, end=' ')
    print()
    t -= 1