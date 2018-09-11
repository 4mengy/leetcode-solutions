# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Queue import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        q = Queue()
        res = []
        q.put(root)
        while q.qsize():
            s = q.qsize()
            t = []
            for _ in range(s):
                curr = q.get()
                t.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            res.append(t)
        return res
        
        