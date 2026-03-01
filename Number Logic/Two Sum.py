def TwoSum():
    num = [1,2,3,4,5,6,7,8,9,10]
    a = num[0]
    b = num[0]
    target = 8
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num [j] == target:
                a = num[i]
                b = num[j]
    return [a,b]
print(TwoSum())