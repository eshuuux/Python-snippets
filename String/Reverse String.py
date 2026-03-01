# s = "My name is Ashish Khote"
# ns = ""
# for i in range(len(s)-1,-1,-1):
#     ns += s[i]
# print(ns)


s = "My name is Ashish Khote"
ns = ""

for ch in s :
    ns = ch + ns
print(ns)