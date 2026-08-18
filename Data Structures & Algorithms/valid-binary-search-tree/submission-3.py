# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       # Here we need to check if the root is not empty 
        if not root:
            return True
       
        q = deque([(root, float("-inf"), float("inf"))])
        while q:

            # So here we are just picking up the left last node 
            node, left, right = q.popleft()
            # Here we are checking the range 
            if not(left < node.val < right):
                return False
            #  Which means the three values are stored here    
            if node.left:
                q.append((node.left,left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        
        return True