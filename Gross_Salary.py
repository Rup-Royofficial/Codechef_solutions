for i in range(int(input())):
    basic_salary = int(input())
    if basic_salary<1500:
        hra_1 = 0.1*basic_salary
        da_1 = 0.9*basic_salary
        print(basic_salary+da_1+hra_1)
    else:
        hra_2 = 500
        da_2 = 0.98*basic_salary
        print(basic_salary+da_2+hra_2)