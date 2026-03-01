s = "Ashish Khote"
ns = ""
for ch in s :
    if ch>= "A" and ch <= "Z" :
        ns += chr(ord(ch)+32)
    elif ch >= "a" and ch <= "z" :
        ns += chr(ord(ch)-32)
    else :
        ns += ch
print(ns)