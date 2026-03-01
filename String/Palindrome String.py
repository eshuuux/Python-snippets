# s = "Naman"
# ns = ""
# for i in range(len(s)-1,-1,-1):
#     ns = ns + s[i]

# if s.lower() == ns.lower() :
#     print("Palindrome")
# else :
#     print("Non Palindrome")

class Solution:
    def isPalindrome(self, s):
        n = len(s)
        left = 0
        right = n -1 
        while left < right :
            if s[left] != s[right] :
                return False
            left += 1
            right -= 1
        return True
if __name__ == "__main__" :
    obj = Solution()
    s = "naman"
    print(obj.isPalindrome(s))