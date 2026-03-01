import numpy as n

a = n.array([10,20,30,40,50,60,70,80,90,100])
largest = a[0]
smallest = a[0]

for i in range(0,len(a)):
    if a[i] > largest :
        largest = a[i]
    if a[i] < smallest :
        smallest = a[i]
print(largest)

second_largest = smallest
for i in range (0, len(a)):
    if a[i] < largest and a[i] > second_largest :
        second_largest = a[i]
print(second_largest)

third_largest = smallest
for i in range (0, len(a)):
    if a[i] < second_largest and a[i] > third_largest :
        third_largest = a[i]
print(third_largest)

fourth_largest = smallest
for i in range (0,len(a)):
    if a[i] < third_largest and a[i] > fourth_largest :
        fourth_largest = a[i]
print(fourth_largest)