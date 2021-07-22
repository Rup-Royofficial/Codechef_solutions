for i in range(int(input())):
    l = []
    a = int(input())
    b = list(map(int, input().split()))
    minimum_of_b = min(b)
    l.append(minimum_of_b)
    b.remove(minimum_of_b)
    minimum_of_b_1 = min(b)
    l.append(minimum_of_b_1)
    print(sum(l))
