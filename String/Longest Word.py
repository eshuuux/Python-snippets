s = "My name is Ashish Khote"
word = s.split()
longest = word[0]
for ch in word:
    if len(ch) > len(longest):
        longest = ch
print(longest)