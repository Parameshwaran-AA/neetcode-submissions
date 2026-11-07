class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        # so we need to sort the intervals by the first of the list start position
        intervals.sort(key=lambda x: x[0])
        # since first one would be the 0th position 
        output = [intervals[0]]

        for start,end in intervals:

            # lastend stores last interval end in output
            lastEnd = output[-1][1]


            # it checks whether the interval of start is less than the last end then it takes 
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        