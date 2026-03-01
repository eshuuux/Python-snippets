base = int(input("Enter Base value : "))
exponent = int(input("Enter Exponential value : "))
result = 1

for i in range(exponent):
    result = result * base
print(result)