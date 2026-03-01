arr = [0,1,2,3,4,5,6,7,8,9,10]
n = len(arr)
left = 0
right = n -1
for i in range(n):
    arr[right],arr[left] = arr[left],arr[right]
    left = left +1
    right -= 1
    print(arr)
    break