# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if p is None and q is None:
                return True

            if p is None:
                return False

            if q is None:
                return False

            if p.val == q.val:
                return same_tree(p.left, q.left) and same_tree(p.right, q.right)

            return False


        def dfs(node):
            if node is None:
                return False

            if node.val == subRoot.val and same_tree(node, subRoot):
                return True

            
            return dfs(node.left) or dfs(node.right)


        if root is None and subRoot is None:
            return True

        if subRoot is None:
            return False

        return dfs(root)

            

        
            