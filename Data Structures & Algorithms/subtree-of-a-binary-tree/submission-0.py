# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to write an queue here
        if not subRoot:
            return True
        if not root:
            return False
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val and self.sameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    

    def sameTree(self, a_root, self_root) -> bool:
        qa,qb = deque([a_root]), deque([self_root])
        while qa:
            a, b = qa.popleft(), qb.popleft()

            if not a and not b:
                 continue
            
            if not a or not b or a.val != b.val:
                return False
            

            qa.append(a.left)
            qa.append(a.right)
            qb.append(b.left)
            qb.append(b.right)
        return True



        