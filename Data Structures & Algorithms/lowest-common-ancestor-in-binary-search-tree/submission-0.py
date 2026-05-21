# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return False

            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node

            if node.val == p.val or node.val == q.val:
                return node

            if l:
                return l

            if r:
                return r

            return None

            

        return dfs(root)


            

        