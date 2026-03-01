a = [10,20,30,40,50]
maxx = a[0]
second_max = a[0]
third_max = a[0]
for i in range (0, len(a)):
    if a[i] > maxx:
        maxx = a[i]
print(maxx)
for i in range(0, len(a)):
    if a[i] < maxx and a[i] > second_max:
        second_max = a[i]
print(second_max)
for i in range(0, len(a)):
    if a[i] < maxx and a[i] < second_max and a[i] > third_max:
        third_max = a[i]
print(third_max)
