class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []


        def backtracking(i, combination, total):

            # If we find the total then we need to append them to the combination by creating a copy of that combination because 
            #that may change after
            if  total == target: 
                result.append(combination.copy())
                return
            

            # if the target is exceeded or ran out of numbers
            if total > target or i  == len(nums):
                return
            

            # Take the current number
            combination.append(nums[i])
            backtracking(i, combination, total + nums[i])


            # Popping out the number because we may got that number into the list need to try again other number or it is not that number
            combination.pop()

            # Again backtracking with the next number i+1 
            backtracking(i+1, combination, total)
        


        backtracking(0, [], 0)

        return result




        