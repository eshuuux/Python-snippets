a = [1,2,3,4,5,0,6,7,8,9,10]
smallest = a[0]
for i in range (0,len(a)):
    if a[i] < smallest :
        smallest = a[i]
print(smallest)