# This method of Reccursion is also know as the tail reccursion or Back tracking

def func(i,n):
    if i > n :
        return 
    func(i + 1, n)
    print(i)
func(1, 10)