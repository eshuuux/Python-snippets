class Solution():
    def ReverseArray(self,arr,left,right):
        left -= 1
        right -= 1
        def reverse(left,right):
            if left>=right :
                return
            arr[left],arr[right] = arr[right],arr[left]
            reverse(left+1,right-1)
        reverse(left,right)
        return arr
if __name__ == "__main__" :
    obj = Solution()
    arr = [1,2,3,4,5]
    left = 1
    right = 2
    print(obj.ReverseArray(arr,left,right))