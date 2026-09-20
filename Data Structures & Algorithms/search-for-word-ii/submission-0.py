class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Creating a node here 
        root = {}
        
        for w in words:
            node = root 
            for ch in w:
                node = node.setdefault(ch, {})
            node["$"] = w
        

        rows, cols = len(board), len(board[0])
        found =[]

        def dfs(r,c,parent):
            # So here we are having row and column from the board 
            ch = board[r][c]
            # node is where we are getting the character if it is there in the board from the root
            node = parent.get(ch)

            # checking the node is none 
            if node is None:
                return
            
            # if not checking the node has a end word $ 
            if "$" in node:
                found.append(node.pop("$"))
            
            # we are just # hashing out the variable so that we do not want to visit them
            board[r][c] = "#"

            # this checks the left side, top, bottom, right side
            for nr, nc in ((r-1,c),(r+1,c), (r,c+1), (r,c-1)):
                # checking if it is outside of index
                if 0 <= nr < rows and 0<= nc < cols:
                    dfs(nr,nc,node)
            
            board[r][c] = ch

            if not node:
                parent.pop(ch)
            
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        
        return found



        