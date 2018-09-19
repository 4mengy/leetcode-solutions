# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def r(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
                
            if left.val != right.val:
                return False
            return r(left.left, right.right) and r(left.right, right.left)
        
        return r(root, root)
        