a = [1,2,3,4,5]
n = len(a)
k = 2

for _ in range(k):
    last = a[n-1]
    for i in range(n-1,0,-1):
        a[i] = a[i-1]
    a[0] = last
print(a)