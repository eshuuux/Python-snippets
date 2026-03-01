s = "My name is Ashish Khote & i'm from yavatmal"
ns = ""
for ch in s :
    if ch >= "A" and ch <= "Z" :
        ns += chr(ord(ch)+32)
    else :
        ns += ch
print(ns)