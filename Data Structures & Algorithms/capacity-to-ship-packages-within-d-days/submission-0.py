class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        # We are using the binary search for the algo 

        # left should be the least capacity
        # Right should be the highest capacity for a day 

        left = max(weights)
        right = sum(weights)

        # then we are declaring a function here 

        def can_ship(capacity):
            
            # how many days needed. We need minimum numbers hence using binary search .
            days_needed = 1
            current_load = 0

            # looping the weights
            for weight in weights: 
                if current_load + weight > capacity : 
                    # then we need to add that in different day and set the current load as zero 
                    current_load = 0
                    days_needed +=1
                
                current_load += weight
            
            # returning this statement to make the right to mid or left to mid to get the minimum days to ship the package
            return days_needed <= days
        


        while left < right:

            mid = (left + right ) // 2
            
            if can_ship(mid):

                right = mid 
            
            else:
                left = mid + 1
        
        return left
        