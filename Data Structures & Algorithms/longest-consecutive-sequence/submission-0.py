class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # first we are creating a set here 
        sethere = set(nums)
        
        # init a variable to store the longest 
        longest = 0

        for num in sethere:

            if(num -1) not in sethere:

                length = 1

                while(num+length) in sethere:

                    length +=1
                longest = max(length, longest)
        
        return longest


        
        