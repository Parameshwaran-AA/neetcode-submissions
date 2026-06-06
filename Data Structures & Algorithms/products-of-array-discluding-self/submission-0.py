class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a list that has everything one 
        res  = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # we are storing the prefix here 
            res[i] = prefix 
            
            # prefix should be multiplied with previous number
            prefix *= nums[i]
        
        #Now we are multiplying the postfix 
        postfix = 1
        for j in range(len(nums)-1, -1, -1):

            # res should store after value of the postfix
            res[j] *= postfix

            # the postfix will be calculated like prefix 
            postfix *= nums[j]

        return res

        