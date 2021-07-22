for i in range(int(input())):
    cnt = int(input())
    words = input("")
    if "Y" in words:
        print("NOT INDIAN")
    elif "I" in words:
        print("INDIAN")
    else:
        print("NOT SURE")