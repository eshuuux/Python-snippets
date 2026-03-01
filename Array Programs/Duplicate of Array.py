a = [1,1,2,3,4,4,5,4,5,6,5,5,5,8,8,7,10,9,9,9,1,2,3,5,4,66,66,5]
n = len(a)

for i in range(n):
    duplicate = False
    for j in range(i):
        if a[i] == a[j]:
            duplicate = True
    
    if duplicate :
        continue 

    for k in range(i+1, n):
        if a[i] == a[k] :
            print(a[i], end=" ")
            break

