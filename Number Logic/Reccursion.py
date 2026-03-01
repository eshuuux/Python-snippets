# def greet():
#     print("Ashish Khote")
#     greet()
# greet()

def greet(count=0):
    if count == 5:
        return
    print("Ashish Khote")
    greet(count + 1)
greet()