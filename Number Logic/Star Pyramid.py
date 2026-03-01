n = int(input("Enter an number : "))
for i in range(0,n+1):
    for j in range (0, n-i-1):
        print("", end ="")
    for k in range(0, i+1):
        print("*",end="")
    print()