class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    
        

    def search(self, word: str) -> bool:

        def dfs(i,node):
            if i == len(word):
                return node.is_end
            

            # Here we are taking the each word here.
            ch = word[i]

            # looping through each word if it has . 
            if ch == '.':
                for child in node.children.values():
                    if(dfs(i+1, child)):
                        return True
                return False
            
            # A normal letter : Only one branch is allowed

            if ch not in node.children:
                return False
            
            return dfs(i+1, node.children[ch])
        return dfs(0,self.root)









        
