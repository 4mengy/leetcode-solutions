# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(root):
            if not root:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            invert(root.left)
            invert(root.right)
            
        invert(root)
        return root
        