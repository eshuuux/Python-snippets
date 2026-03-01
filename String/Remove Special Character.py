s = "Today's Price !! $80 Only"
n = ""
for ch in s :
    if (ch >= "a" and ch <="z") or (ch >= "A" and ch <= "Z") or (ch >= '0' and ch <='9') or (ch == " "):
        n = n + ch
print(n)