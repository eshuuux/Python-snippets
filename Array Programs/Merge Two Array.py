a = [1,2,3,4,5]
b = [6,7,8,9,10]
# n1 = len(a)
# n2 = len(b)

# c = [0] * (n1 + n2)

# for i in range(len(a)):
#     c[i] = a [i]

# for j in range(len(b)):
#     c[n1 + j] = b[j]

# print(c)


n1 = len(a)

c = [0] * n1*2

for i in range(n1):
    c[i] = a[i]

for j in range(n1):
    c[j+n1] = b[j]

print(c)