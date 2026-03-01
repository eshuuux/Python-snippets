a = [10,20,30,40,50,60,70,80,90]
largest = a[0]

for i in range (0,len(a)) :
    if a[i] > largest :
        largest = a[i]
print(largest)
