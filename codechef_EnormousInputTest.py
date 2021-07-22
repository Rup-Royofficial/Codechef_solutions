n,k = map(int,input().split())          #two integer inputs side by side

count = 0
for i in range(n):                      #in the range of the input (n) ; je number ache to to bar loop cholbe 
    e = int(input())                    # again input
    if e%k == 0:                        # checks if divisible
        count += 1

print(count)        