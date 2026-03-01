def TripletSum():
    num = [0,1,2,3,4,5,6,7,8,9,10]
    a = num[0]
    b = num[0]
    c = num[0]
    target = 5
    for i in range (len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i] + num[j] + num[k] == target:
                    a = num[i]
                    b = num[j]
                    c = num[k]
    return [a,b,c]
print(TripletSum())