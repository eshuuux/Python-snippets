class Solution():
    def Palindrome(self,s,left,right):
        if left > right :
            return True
        if s[left] != s[right] :
            return False
        return self.Palindrome(s,left+1,right-1)
if __name__ == "__main__" :
    obj = Solution()
    s = "Naman"
    left = 0
    right = len(s)-1
    print(obj.Palindrome(s,left,right))