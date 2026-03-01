a = [1,2,3,4,5,5,8,6,7,9,7,620,21,2]
# even_count = 0
# odd_count = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0 :
#         even_count += 1
#     if a[i] % 2 != 0 :
#         odd_count += 1
# print(f"The Total Count Of Evens Are {even_count} & Total Odds Are {odd_count}")


even_count = 0
odd_count = 0

for i in range(len(a)):
    if a[i]%2==0 :
        even_count += 1
    if a[i]%2!=0 :
        odd_count += 1

print(f"The Even count are {even_count} and Odd counts are {odd_count}")