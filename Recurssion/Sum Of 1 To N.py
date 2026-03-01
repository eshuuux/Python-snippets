# Also known as parameterized function
def func(total,i,n):
    if i > n :
        print(total)
        return
    func(total + i, i + 1, n)
func(0, 1 , 10)