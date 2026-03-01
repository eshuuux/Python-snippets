import math
num = int(input("Enter an Input : "))
temp = num
rev = 0
while temp>0:
    digit = temp % 10
    rev = rev*10 + digit
    temp = temp // 10
if rev == num:
    print("Palindrome")
else:
    print("Not an Palindrome")
