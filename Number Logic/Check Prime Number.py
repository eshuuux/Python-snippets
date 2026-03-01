def Primecheck():
    n = int(input("Enter an valid value : "))
    for i in range (2, n):
        if n % i == 0:
            print("Is Non-Prime")
            break
    else :
        print("Prime")
Primecheck()