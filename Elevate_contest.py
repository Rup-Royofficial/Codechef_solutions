count= 0
for i in range(0,100):
    x = i*i
    y = i
    if (x+y+1)%91==0:
        count+=1
        
print(count)