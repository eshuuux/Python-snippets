s = "Python Programming"
n = len(s)
for i in range(n):
    duplicate = False
    for j in range (i):
        if s[i] == s[j]:
            duplicate = True
    if duplicate :
        continue
    for k in range(i+1, n):
        if s[i] == s[k] :
            print(s[i], end="")
            