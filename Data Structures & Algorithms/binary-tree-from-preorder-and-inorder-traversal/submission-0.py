# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Here we start the comprhension 
        mapping  = {val:ind for ind,val in enumerate(inorder)}

        # We init a moving index 
        self.move = 0 

        def dfs(left, right):

            if left > right :
                return None
            
            # initializing and getting the first root node
            root_val = preorder[self.move]

            # increase the root node 
            self.move += 1

            # Then we need to build the tree
            root = TreeNode(root_val)

            # then we need to split that using the logic 
            # find the middle in the hash and left belongs to left subtree and right to right subtree
            mid = mapping[root_val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1 , right)
            return root 
        

        return dfs(0, len(inorder)- 1)