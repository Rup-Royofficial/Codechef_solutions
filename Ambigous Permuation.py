while True:
    t = int(input())
    if t==0:
        break
    else:
        l = list(map(int,input().split()))
        inv_list = [i for i in range(t)]
        for i,j in enumerate(l):
            inv_list[j-1] = i+1
        if inv_list==l:
            print("ambiguous")
        else:
            print("not ambiguous")
