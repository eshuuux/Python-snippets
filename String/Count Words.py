s = "My name is Ashish Khote and i'm from Yavatmal"
count = 0
in_words = False
for ch in s :
    if ch != " " and not in_words :
        count += 1
        in_words = True
    elif ch == " " :
        in_words = False
print(count)

# s = "My Name is Ashish Khote and I'm From Yavatmal"
# words = s.split()
# print(len(words))