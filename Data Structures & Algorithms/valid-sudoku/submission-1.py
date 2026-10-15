class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Passing only row 
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # Passing only col
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        

        # 3 * 3 box
        # incrementing thrice
        for start_row in range(0,9,3):
            for start_col in range(0,9,3):
                seen = set()
                
                # Here now we are going through each numbers in the box 
                for r in range(start_row,start_row+3):
                    for c in range(start_col,start_col+3):

                        if board[r][c] == '.':
                            continue
                        if board[r][c] in seen:
                            return False
                        
                        seen.add(board[r][c])
        return True


                    
        