
n = int(input())
d = []
f = []
x = 0
y = 0
c_1 = []
c_2 = []

for i in range(n):
    a,b = map(int,input().split())
    if a>b:
        c = a-b
        d.append(c)
        c_1.append(a)
        c_2.append(b)

    if b>a:
        e = b-a
        f.append(e)
        c_1.append(a)
        c_2.append(b)

    

if sum(c_1)> sum(c_2):
    print(f"1 {max(d)}")

if sum(c_2)>sum(c_1):
    print(f"2 {max(f)}")                 

"""
p1=[0]
p2=[0]
q1=0
q2=0
for i in range(int(input())):
    a,b=map(int,input().split())
    q1+=a
    q2+=b
    s=q1-q2
    if s>=0:
        p1.append(s)
    else:
        p2.append(-s)
# print(p1,p2)
p1=max(p1)
p2=max(p2)
if p1>=p2:
    print(1,p1)
else:
    print(2,p2)    
"""

""" this above code is the correct answer as per them"""
"""although  the question  is broken , i think """    