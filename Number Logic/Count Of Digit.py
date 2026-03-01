from math import log10

# num = int(input("Enter an Number : "))
# temp = num
# count = 0
# while (temp>0):
#     temp = temp // 10
#     count +=1
# print(count)

num = int(input("Enter an integer : "))
temp = num
print(int(log10(num)+1))  #The LOG10 Gives Value Like Log10(123) = 2.756 + 1 = 3.756 Then Type Casting