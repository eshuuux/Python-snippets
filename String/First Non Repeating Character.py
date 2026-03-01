s = "swwizeese"
ns = ""
n = len(s)
for i in range(n):
    repeat = False
    for j in range(i):
        if s[i] == s[j] :
            repeat = True
    for k in range (i+1,n):
        if s[i] == s[k]:
            repeat = True
    if not repeat :
        print(s[i])
        break