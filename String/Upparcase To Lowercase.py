s = "My name is Ashish Khote"
ns = ""
for ch in s :
    if (ch >= "a" and ch <= "z"):
        ns += chr(ord(ch)-32)
    else:
        ns += ch
print(ns)