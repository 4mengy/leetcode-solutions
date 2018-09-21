# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return True, None, None
            
            if root.left and not root.left.val < root.val:
                return False, None, None
            
            if root.right and not root.val < root.right.val:
                return False, None, None
            
            l_ret, l_min_v, l_max_v = check(root.left)
            r_ret, r_min_v, r_max_v = check(root.right)
            
            if not l_ret or not r_ret:
                return False, None, None
            
            if l_max_v and not l_max_v < root.val:
                return False, None, None
            
            if r_min_v and not root.val < r_min_v:
                return False, None, None
            
            return True, l_min_v if l_min_v else root.val, r_max_v if r_max_v else root.val 
            
        
        return check(root)[0]
                