arr = [1,2,3,4,5,6,7,8]
hash_map = {}
for i in range(len(arr)):
    hash_map[arr[i]] = hash_map.get(arr[i],0)+1
print(hash_map)