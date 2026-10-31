class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # we need one element to store the prefix sum 
        prefix_sum = 0
        
        # returning the count 
        count = 0 

        # Here we are init the frequency 
        frequency = {0:1}

        # now we are looping through 
        for num in nums:

            # adding up the sum 
            prefix_sum += num

            # checking there is a prefix sum is there or not 
            needed = prefix_sum - k

            # now updating the count 
            count += frequency.get(needed, 0)

            # if not then we are updating the prefix sum else init the prefix sum to the new hash map
            frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1
        

        return count



        