class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # this is the input graph for the undirected one 
        graph = {i: [] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for i in graph[node]:
                dfs(i)
        


        count = 0

        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        
        return count
        



        