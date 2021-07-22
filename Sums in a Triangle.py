l = []
for i in range(int(input())):
    second_count = int(input())
    for j in range(second_count):
        third_count = list(map(int, input().split()))
        for k in third_count:
            l.append(k)
        l_1 = sum(l)
        print(l_1)
