n = int(input("Enter an value to check, "))
print(f"The factors of {n} is")

for i in range(1,n+1):
    if n % i == 0 :
        print(i, end=" ")