#Python program find factorial of a number
#using while loop
n = int(input())
for i in range(n):
    num=int(input())
#takes input from user
    factorial=1;  #declare and initialize factorial variable to one
#check if the number is negetive ,positive or zero
    if num<0:
        print("Factorial does not defined for negative integer");
    elif(num==0):
        print("The factorial of 0 is 1");
    else:
        while(num>0):
            factorial=factorial*num
        
            num=num-1
        
#print("factorial of the given number is: ")
    print(factorial)


#decipher it later
#made by me below
'''
import math
t = int(input())
for i in range(t):
    x = int(input())
    print(math.factorial(x))
'''    