s = "Ashish Khote"
n = len(s)

for i in range(n):
    duplicate = False
    for j in range(i):
        if s[j] == s[i] :
            duplicate = True
    if not duplicate :
        print(s[i], end="")