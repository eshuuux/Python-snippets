s = "Ashish Khote"
for i in range(len(s)):
    seen = False
    count = 1
    for j in range(i):
        if s[i] == s[j] :
            seen = True
    if seen :
        continue
    for k in range(i+1, len(s)):
        if s[i] == s[k]:
            count += 1
    print(s[i], "->" ,count)