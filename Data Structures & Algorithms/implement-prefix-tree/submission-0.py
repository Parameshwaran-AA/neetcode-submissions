class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word: str) -> None:
        # we need to start witht the cur
        cur = self.root

        # loop through each current 
        for each in word:
            if each not in cur.children:
                cur.children[each] = TrieNode()
            cur = cur.children[each]
        
        cur.endOfword = True


    def search(self, word: str) -> bool:

        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur.endOfword


        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root 

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
        
        