a = [1,2,3,4,5,6,7,8]
n = len(a)
summ = 0

for i in range(len(a)):
    summ = summ + a[i]

avg = summ / n
print(avg)