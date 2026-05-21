# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = root
        stack = []
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left


            node = stack.pop()
            if prev is not None and node.val <= prev:
                return False

            prev = node.val
            curr = node.right

        return True


            
