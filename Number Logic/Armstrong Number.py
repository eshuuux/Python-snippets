n = int(input("Enter a valid input : "))
rev = 0
nod = len (str(n))
while n > 0 :
    digit = n % 10
    rev = rev + ( digit ** nod )
    n = n // 10
print(rev)