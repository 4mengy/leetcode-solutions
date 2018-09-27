"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from Queue import Queue

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = Queue()
        queue.put(root)
        ret = []
        
        while not queue.empty():
            size = queue.qsize()
            tmp = []
            for _ in range(size):
                curr = queue.get()
                tmp.append(curr.val)
                for item in curr.children:
                    queue.put(item)
            ret.append(tmp)
        return ret
    