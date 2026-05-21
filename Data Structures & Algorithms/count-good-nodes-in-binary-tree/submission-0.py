# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, val):
            nonlocal count
            if node is None:
                return

            new_val = val

            if node.val >= val:
                count += 1
                new_val = node.val
            
            dfs(node.left, new_val)
            dfs(node.right, new_val)


        dfs(root, -101)

        return count