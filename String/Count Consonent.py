s = "I'm Ashish Khote"
count = 0
for ch in s :
    if ( ch >= "a" and ch <= "z" ) or ( ch >= "A" and ch <= "Z" ):
        if ch.lower() not in "aeiou" :
            count += 1
print(count)

# s = "I'm Ashish Khote"
# count = 0
# for ch in s :
#     if ch.isalpha() and ch.lower() not in "aeiou" :
#         count += 1
# print(count)