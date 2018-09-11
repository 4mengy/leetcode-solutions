# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def r(root, deth):
            if root is None:
                return deth
            
            deth += 1
            return max(r(root.left, deth), r(root.right, deth))
        
        return r(root, 0)
            
        