class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows =  len(board)
        cols = len(board[0])
        visited = set()

        def backtracking(r, c, index):
            

            # If the index reached the length of the word then only this function returns True
            if index  == len(word):
                return True


            # For simplicity we are dividing the if statement to understand better

            # this is out of bound If statement 
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            

            # This one if the current r and c is not found then we need to return False
            if board[r][c] != word[index]:
                return False


            # if the board found already visited i.e marked as # should be ignored so returning False
            if board[r][c] == '#':
                return False

            
            # Marking the board # 
            board[r][c] = '#'
            res = (
            backtracking(r+1, c, index + 1) or
            backtracking(r-1, c, index + 1) or
            backtracking(r, c-1, index + 1) or
            backtracking(r, c+1, index + 1) )


            # Reassigning back them to the same word. Only found words we will change into # 
            board[r][c] = word[index]
            return res
            
            
            

           
            

        for i in range(rows):
                for j in range(cols):
                    if backtracking(i, j, 0):
                        return True
        return False

        