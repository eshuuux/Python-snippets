a = [1,2,3,4,5]
n = len(a) + 1
summ = 0
total = n * (n+1) // 2

for i in a:
    summ = summ + i

missing = total - summ
print(missing)
