"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            elif not root.children:
                return 1
            
            return max(map(depth, root.children)) + 1
        
        return depth(root)
    