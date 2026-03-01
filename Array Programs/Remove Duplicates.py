a = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
n = len(a)

for i in range(len(a)):
    duplicate = False
    for j in range (i):
        if a[j] == a[i] :
            duplicate = True
    
    if not duplicate:
        print(a[i], end=" ")