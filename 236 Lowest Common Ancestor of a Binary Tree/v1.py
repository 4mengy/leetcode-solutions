# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def check(node):
            curr = None
            if not node:
                return
            elif node is p or node is q:
                curr = True
                
            lc = check(node.left)
            rc = check(node.right)
            
            if (lc and rc) or (curr and (lc or rc)):
                return node
            elif lc: return lc
            elif rc: return rc
            elif curr: return curr
            
        return check(root)
        