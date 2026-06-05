class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # loop until i < length of the string 
        while i < len(s):

            # let equate i = j 
            # i is the start of the next . j is the start of the word 
            j = i

            while s[j] != '#':
                j += 1
            
            # we are stopping when we get # and then retrieving the length of the word 
            length = int(s[i:j])

            word = s[j+1 : j+1+length]

            res.append(word)
            i = j+1 + length 
        return res

