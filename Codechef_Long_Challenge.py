"""
for i in range(int(input())):
    X,A,B = map(int,input().split())
    c = A+(100-X)*B
    print(c*10)

"""
"""
for i in range(int(input())):
    N,x,k = map(int,input().split())
    a = 0
    l = []
    for j in range(x):
        l.append(a)
        a+=k
    if x in l:
        print("YES")
    else:
        print("NO")
"""
def myfunction(new1,new2,new3):
	myresult=1
	new1=new1%new3
	if new1==0:
		return 0
	while new2>0:
		if (new2 & 1):
			myresult= (myresult*new1)%new3
		new2=new2>>1
		new1=(new1*new1)%new3
	return(myresult)

mymod=1000000007
test=int(input())
for _ in range(test):
	n = int(input())
	myans=myfunction(2,n-1,mymod)
	print(myans)