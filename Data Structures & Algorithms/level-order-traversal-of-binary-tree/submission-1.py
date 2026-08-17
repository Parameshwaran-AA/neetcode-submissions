# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        if not root:  
            return []
        else:
            q1 = deque([root]) 
            while q1:
                result2  =  [] 
                length = len(q1)
                for _ in range(length):
                    current  = q1.popleft()
                    result2.append(current.val)
                    if current.left:
                       q1.append(current.left)
                    if current.right:
                       q1.append(current.right)
                result.append(result2)
            
        return result
            
            


    
        