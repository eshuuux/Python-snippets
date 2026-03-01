n = int(input("Enter an value :"))
rev = 0     # For Multiplying Just Add rev = 1 and change sign for rev = rev * digit
while (n >0):
    digit = n % 10 
    rev = rev + digit
    n = n // 10
print(rev)