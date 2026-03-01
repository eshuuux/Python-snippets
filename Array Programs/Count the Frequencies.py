a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

# for i in range(len(a)):
#     count = 1
#     visited = False
#     for j in range(i) :
#         if a[i] == a[j] :
#             visited = True
    
#     if visited :
#         continue 

#     for k in range(i+1 ,n):
#         if a[i] == a[k] :
#             count += 1
#     print(a[i],"->",count)


for i in range(len(a)):
    visited = False
    count = 1

    for j in range(i):
        if a[i] == a[j]:
            visited = True
    
    if visited :
        continue

    for k in range(i+1, len(a)):
        if a[k] == a[i]:
            count += 1
    print(a[i],"->",count)