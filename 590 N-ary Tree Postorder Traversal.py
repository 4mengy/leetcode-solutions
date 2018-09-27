"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack = [root]
        visited = set()
        ret = []
        while stack:
            curr = stack[-1]
            if curr.children and curr not in visited:
                stack.extend(filter(lambda x: x, curr.children[::-1]))
                visited.add(curr)
            else:
                stack.pop()
                ret.append(curr.val)
        return ret
                