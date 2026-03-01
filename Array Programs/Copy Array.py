# a = [1,2,3,4,5]
# b = [0] * len(a)
# i = 0

# while i < len(a):
#     b[i] = a[i]
#     i = i + 1
# print("Original :",a)
# print("Copied :",b)


a = [10,20,30,40,50]
b = [0] * len(a)

for i in range(len(a)):
    b[i] = a[i]

print(b)