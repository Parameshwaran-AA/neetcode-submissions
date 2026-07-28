class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  = 0 
        right = len(nums)-1
        #minimum = float('inf')
        mid = 0

        while(left < right):
            mid = (left + right) // 2

            if(nums[mid] < nums[right]):
                #minimum = min(minimum,nums[mid])
                right = mid
                
            else:
                #minimum = min(nums[left],minimum)
                left = mid + 1
                

        return nums[left]



        