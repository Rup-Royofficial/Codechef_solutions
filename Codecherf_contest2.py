"""
MAX_CHAR = 26


# Utility function to find factorial of n.
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact


# Returns count of distinct permutations
# of str.
def countDistinctPermutations(st):
    length = len(st)
    freq = [0] * MAX_CHAR

    # finding frequency of all the lower
    # case alphabet and storing them in
    # array of integer
    for i in range(0, length):
        if (st[i] >= 'a'):
            freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1

    # finding factorial of number of
    # appearances and multiplying them
    # since they are repeating alphabets
    fact = 1
    for i in range(0, MAX_CHAR):
        fact = fact * factorial(freq[i])

    # finding factorial of size of string
    # and dividing it by factorial found
    # after multiplying
    return factorial(length) / fact


# Driver code
st = "aabbcde"
print(countDistinctPermutations(st))

from itertools import permutations


def allPermutations(str):
    # Get all permutations of string 'ABC'
    permList = permutations(str)
    count = 0
    # print all permutations
    for perm in list(permList):
        print(''.join(perm))
        count +=1
        print(count)


# Driver program
if __name__ == "__main__":
    str = 'aabbcde'
    allPermutations(str)

x = 2021
y = x*x*x*x*x*x*x*x*x*x
print((y+1)%4080400)
"""
x = 2
print(x**32582657+1)