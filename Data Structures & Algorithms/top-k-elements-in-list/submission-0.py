class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # we are initialized the dictionary here
        freq = {}

        # we will loop the nums and go for each number and adding it into the dictionary 
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        sorted_nums = sorted(
                freq, key = freq.get, reverse = True)

        
        return sorted_nums[:k]
        
        