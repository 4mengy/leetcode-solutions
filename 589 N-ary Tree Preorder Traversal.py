"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        ret = []
        while stack:
            curr = stack.pop()
            ret.append(curr.val)
            if curr.children:
                stack.extend(filter(lambda x: x, curr.children[::-1]))
        return ret

            
        