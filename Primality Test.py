try:
    def check_prime(number):
        if number==1 or number<1:
            return False
        else:
            for i in range(2, number):
                if number%i==0:
                    return False
        return True

    t = int(input())
    for _ in range(t):
        number = int(input())
        if check_prime(number):
            print("yes")
        else:
            print("no")
except:
    pass