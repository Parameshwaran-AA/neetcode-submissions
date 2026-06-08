class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # initialize the list to return 
        result = []

        # Step 1 We need to sort the given list 
        nums.sort()

        # now start from the index 
        for i in range(len(nums)-2):

            # we need to skip the pivot element 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            
            left = i +1
            right = len(nums)-1
            # we are checking with the pointers by left and right

            while(left < right):

                total = nums[i] + nums[left] + nums [right]
                # since this is sorted, if sum is small then increment the left 
                if(total < 0):
                    left += 1
                elif(total > 0):
                    right -= 1
                else:
                    # where we find the triplets here 
                    result.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    right -= 1
                    # here if there is a duplicate triplet we need to ignore that

                    while(left < right and nums[left] == nums[left - 1] ): left += 1
                    while(left < right and nums[right] == nums[right + 1]): right -= 1

        return result




                    




        