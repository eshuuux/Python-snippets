def func(i, n):
    if i < n :
        return 
    func(i-1, n)
    print(i)
func(10,1)