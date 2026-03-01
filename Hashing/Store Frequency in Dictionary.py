arr = [1,1,2,5,4,5,1,2,4,5,2,3,3,6,5,4,5,6,3,3]
freq_map = {}
for i in range(len(arr)):
    if arr[i] in freq_map :
        freq_map[arr[i]] += 1
    else :
        freq_map[arr[i]] = 1
print(freq_map)