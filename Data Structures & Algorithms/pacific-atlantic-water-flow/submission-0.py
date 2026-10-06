class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # going to allocate rows and columns for this 
        rows, cols = len(heights), len(heights[0])

        # then we are going to create a set to store individ
        pac, atl = set(), set()

        def dfs(r, c, seen, prev):

            # This is a if statement checks for the r and c reaches above the limit, lesser than the previous one , if it is 
            # already in the set, if that goes below zero -> killing it 
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in seen or heights[r][c] < prev:
                return
            
            # adding it to the set
            seen.add((r,c))

            # marking for the prev
            h = heights[r][c]

            #checking the grid
            dfs(r+1, c, seen, h)
            dfs(r-1, c, seen, h)
            dfs(r, c+1, seen, h)
            dfs(r, c-1, seen, h)

        


        # this should be like calling the function for first row and last row 
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        # this should be like calling the function for first col and last col 
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])


        #returning if the row and col exists in pac and atl        
        return[[r,c] for r,c in pac & atl]


        