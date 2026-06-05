class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)

        for word in strs:

            # now we are looping the words in the list of strs and then sorting out 
            w  = "".join(sorted(word))
            group[w].append(word)
        
        return list(group.values())

        