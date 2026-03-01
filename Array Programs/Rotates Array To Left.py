a = [1,2,3,4,5]
n = len(a)
k = 2

for _ in range(k):
    first = a[0]
    for i in range(n-1):
        a[i] = a[i+1]
    a[n-1] = first
print(a)