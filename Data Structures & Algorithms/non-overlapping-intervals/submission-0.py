class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # we need to get the sorting 
        # sorting the ending point 
        intervals.sort(key = lambda x: x[1])

        
        # need to define the start, previous end point 
        count = 0
        Total = len(intervals)
        previous_end = float('-inf')


        # looping through the intervals 
        for start, end in intervals: 
            

            if(start >= previous_end):
                count += 1
                previous_end = end
        

        return Total - count
        


        