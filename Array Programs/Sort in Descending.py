a = [11,33,66,55,44,88,77,99,22,110]
n = len(a)

for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j] :
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a, end = " ")