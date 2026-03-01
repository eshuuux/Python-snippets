class Solution():
    def Fib(self,num):
        if num == 0 or num == 1 :
            return num
        return self.Fib(num - 1) + self.Fib(num - 2)
    def Result(self,n):
        answer = self.Fib(n)
        return answer

if __name__ == "__main__":
    obj = Solution()
    n = 9
    print(obj.Result(n))
