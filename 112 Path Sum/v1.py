# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def check(node, s):
            if not node:
                return False
            
            s += node.val
            if s == sum and not node.left and not node.right:
                return True
            
            return check(node.left, s) or check(node.right, s)
        
        return check(root, 0)
        