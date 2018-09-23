# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        oroot = root
        if not root:
            return TreeNode(val)
        
        while True:
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left   
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return oroot
        
                
            