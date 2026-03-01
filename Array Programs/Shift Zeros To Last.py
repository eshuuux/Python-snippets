a = [1, 1, 2, 0, 3, 0, 4]
n = len(a)

j = 0
for i in range(n):
    if a[i] != 0:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j += 1
print(a)