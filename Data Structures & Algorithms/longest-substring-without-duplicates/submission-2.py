class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(len(s) < 1):
            return 0
        length = ""
        substring = 1
        length+=s[0]
        maximum_sub= 1

        for i in range(1,len(s)):

            
            if (s[i] not in length):
                length+=s[i]
                #substring+=1
            else:
                idx = length.index(s[i])      # find earlier copy
                length = length[idx + 1:] 
                #length = "" 
                length +=s[i]
                #substring = 1
            maximum_sub = max(len(length), maximum_sub)
        
        return maximum_sub
            
            
            
            



        