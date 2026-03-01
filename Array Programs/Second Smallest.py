import numpy as a

a = a.array([0,1,20,3,5,4,80,90,70,2,6,1])
largest = a[0]
smallest = a[0]

for i in range(len(a)):
    if a[i] > largest :
        largest = a[i]
    if a[i] < smallest :
        smallest = a[i]
print(f"The Smallest & Largest Elements are {smallest} & {largest}")

second_smallest = largest 
for i in range (len(a)):
    if a[i] > smallest and a[i] < second_smallest :
        second_smallest = a[i]
print(second_smallest)

third_smallest = largest 
for i in range(len(a)):
    if a[i] > second_smallest and a[i] < third_smallest :
        third_smallest = a[i]
print(third_smallest)

fourth_smallest = largest 
for i in range(len(a)):
    if a[i] > third_smallest and a[i] < fourth_smallest :
        fourth_smallest = a[i]
print(fourth_smallest)
