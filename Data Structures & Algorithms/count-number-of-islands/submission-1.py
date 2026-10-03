class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])

        def dfs(r,c):

            # if it is beyond the grid then we are assigning to zero
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            # if there is no one then it is default to zero or else it is visited 
            if grid[r][c] != "1":
                return
            

            # Group of islands is 1 not individual islands. Group is Left right up and down
            # no we should not visit again hence assigning to zero
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1, c)
            dfs(r,c+1)
            dfs(r,c-1)
        

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        
        return count






        