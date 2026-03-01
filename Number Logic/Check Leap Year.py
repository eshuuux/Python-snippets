year = int(input("Enter Year To Check :"))
if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
    print("Its an Leap Year")
else:
    print("Its Not an Leap Year")