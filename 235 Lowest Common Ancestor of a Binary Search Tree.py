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
        def search(root, val):
            if root.val == val:
                return root
            elif val < root.val:
                return root.left
            else:
                return root.right
        pr = root
        qr = root
        last = root
        while True:
            pr = search(pr, p.val)
            qr = search(qr, q.val)
            if pr != qr:
                return last
            last = qr
            
        