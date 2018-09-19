# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def r(root, res):
            if root is None:
                return
            
            r(root.left, res)
            res.append(root.val)
            r(root.right, res)
            
        res = []
        r(root, res)
        return res
        
                
                
        